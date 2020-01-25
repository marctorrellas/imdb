import warnings

import numpy as np
from sklearn.metrics import confusion_matrix


def tnr(y_true, y_pred):
    """
    Compute True Negative Rate given true and predicted labels. In other words,
    (true negatives) / (true negatives + false positives). Two degenerate cases exist:
    If all true's are positive
        - return 0 if any negative prediction (false negative),
        - 1 otherwise, with a warning
    Args:
        y_true (list or array): true labels
        y_pred (list or array): predicted labels

    Returns (float): in [0, 1]

    """
    if not isinstance(y_true, np.ndarray):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)

    if (y_true == 1).all():
        if (y_pred == 1).any():
            return 0
        else:
            msg = (
                "TNR = 1, but no true negatives actually found. That's because "
                "ground truth contains no negatives"
            )
            warnings.warn(Warning(msg))
            return 1

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tn / (tn + fp)
