from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from imdb.models.base_model import BaseModel


class ClassicalModel(BaseModel):

    default_tfidf_kwargs = {"stop_words": "english", "min_df": 3}
    default_lr_kwargs = {"class_weight": "balanced", "solver": "lbfgs", "max_iter": 100}

    def __init__(self, tfidf_kwargs=None, lr_kwargs=None, cv_kwargs=None):
        super().__init__(cv_kwargs=cv_kwargs)
        self.tfidf_kwargs = tfidf_kwargs or self.default_tfidf_kwargs
        self.lr_kwargs = lr_kwargs or self.default_lr_kwargs
        self.tfidf_vectorizer = TfidfVectorizer(**self.tfidf_kwargs)
        self.model = Pipeline(
            [
                ("tfidf", self.tfidf_vectorizer),
                ("lr", LogisticRegression(**self.lr_kwargs)),
            ]
        )


class AlbertModel(BaseModel):

    # TODO: create an sklearn-friendly interface to make this compatible with BaseModel

    default_albert_kwargs = {}

    def __init__(self, albert_kwargs=None, cv_kwargs=None):
        raise NotImplementedError("Albert model not implemented yet")
