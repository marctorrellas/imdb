import logging

import joblib
import pandas as pd
from pathlib import Path

from imdb.config import DEFAULT_DATA_LOCATION

log = logging.getLogger("imdb")


def load_data(data_filename, data_dir, cache_enabled=True, labelled=True):
    if data_filename:
        # TODO: add test for filename not exists
        data = joblib.load(data_filename)
    else:
        if not data_dir:
            log.info(f"Using default data sample in: {DEFAULT_DATA_LOCATION}")
            data_dir = DEFAULT_DATA_LOCATION
        data = load_data_from_dir(Path(data_dir), cache_enabled, labelled=labelled)
    return data


def load_data_from_dir(data_dir, cache_enabled=False, labelled=True):
    # TODO: do we want a configurable location?
    cache_file = data_dir / "cache.joblib"
    if cache_enabled and cache_file.exists():
        log.info(f"Loading data from cache file {cache_file}")
        return joblib.load(cache_file)
    return (
        build_labelled_texts_dataframe(data_dir, cache_enabled, cache_file)
        if labelled
        else pd.DataFrame({"text": read_texts(data_dir)})
    )


def build_labelled_texts_dataframe(data_dir, cache_enabled, cache_file):

    check_imdb_format(data_dir)
    pos_texts = read_texts(data_dir, "pos/*txt")
    neg_texts = read_texts(data_dir, "neg/*txt")
    df = pd.DataFrame({"text": pos_texts + neg_texts, "label": 0})
    df.iloc[: len(pos_texts), 1] = 1
    if cache_enabled:
        log.info(f"Caching data into {cache_file}")
        joblib.dump(df, cache_file)
    return df


def check_imdb_format(data_dir):
    log.info("WARNING! check IMDB TODO")
    return True


def read_texts(data_dir, regex="*txt"):
    texts = []
    for file in data_dir.glob(regex):
        with open(file, "r") as f:
            texts.append(f.read())
    return texts
