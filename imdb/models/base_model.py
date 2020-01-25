import logging
from abc import ABC

import pandas as pd
from sklearn.metrics import (
    make_scorer,
    recall_score,
    accuracy_score,
    confusion_matrix,
    roc_curve,
)
from sklearn.model_selection import cross_validate, KFold, train_test_split

from imdb.config import RANDOM_STATE, CV_TRAIN_SIZE
from imdb.core.metrics import tnr

log = logging.getLogger("imdb")


class BaseModel(ABC):
    """
    An abstract class defining common methods for any kind of model. The model is stored
    in the attribute `model` and it should have an sklearn-friendly interface, e.g.
    `fit`, `predict`, `predict_proba` must be defined.
    """

    default_cv_kwargs = {
        "cv": KFold(3, shuffle=True, random_state=RANDOM_STATE),
        "return_train_score": True,
        # TODO: move to config.py and make n_jobs dependant on number of cores
        "n_jobs": 3,
    }

    split_kwargs = {
        "train_size": CV_TRAIN_SIZE,
        "test_size": 1 - CV_TRAIN_SIZE,
        "random_state": RANDOM_STATE,
    }

    def __init__(self, cv_kwargs=None):
        self.model = None
        self.__scorers = self.__get_scorers()
        self.cv_kwargs = cv_kwargs or self.default_cv_kwargs
        self.cv_kwargs["scoring"] = self.__scorers
        self.threshold = 0.5

    def __get_scorers(self):
        accuracy = make_scorer(accuracy_score)
        tpr = make_scorer(recall_score)
        tnr_scorer = make_scorer(tnr)
        return {"accuracy": accuracy, "tpr": tpr, "tnr": tnr_scorer}

    def train(self, data, cv_enabled=False, calibration_enabled=True):
        """
        Train a binary classifier using data, and optionally doing cross-validation,
        and calibration
        Args:
            data (pd.DataFrame): a dataframe with two columns: text and label
            cv_enabled (bool): If True, cross-validation is carried out
            calibration_enabled (bool): If True, the decision threshold is calibrated
                Otherwise, 0.5 is used as a threshold

        """
        texts, labels = data.text, data.label
        if cv_enabled:
            log.info("Running cross-validation")
            log.debug(cross_validate(self.model, texts, labels, **self.cv_kwargs))
        if calibration_enabled:
            log.info("Running decision threshold calibration")
            self.__calibrate(texts, labels)
        else:
            log.info("Fitting model with all data")
            self.model.fit(texts, labels)

    def __calibrate(self, texts, labels):
        """
        Sets the decision threshold based on maximising accuracy on the validation set,
        with the support of the ROC curve
        """
        texts, x_val, labels, y_val = train_test_split(
            texts, labels, stratify=labels, **self.split_kwargs
        )
        self.model.fit(texts, labels)
        prob_val = self.model.predict_proba(x_val)
        fpr, tpr, thresholds = roc_curve(y_val, prob_val[:, 1])
        idx = (tpr + 1 - fpr).argmax()
        self.threshold = thresholds[idx]
        log.debug(
            f"Optimal threshold: {self.threshold:.2f}, "
            f"fpr: {fpr[idx]:.2f}, "
            f"tnr: {1 - fpr[idx]:.2f}, "
            f"tpr: {tpr[idx]:.2f}, "
            f"accuracy: {(1 - fpr[idx] + tpr[idx]) / 2:.2f}"
        )

    def predict(self, texts):
        probs = self.model.predict_proba(texts)
        return (probs[:, 1] >= self.threshold).astype(int)

    def evaluate(self, data):
        """
        Evaluate the model on given data, showing performance on scorers defined in
        self.scorers and the confusion matrix
        """
        texts, labels = data.text, data.label
        predictions = self.predict(texts)
        cm = confusion_matrix(labels, predictions)
        log.info(
            pd.DataFrame(
                cm, index=["TRUE_NEG", "TRUE_POS"], columns=["PRED_NEG", "PRED_POS"]
            )
        )
        for name, scorer in self.__scorers.items():
            log.info(f"{name}: {scorer._score_func(labels, predictions)}")
