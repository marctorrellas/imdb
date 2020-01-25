import argparse
import logging

import joblib

from imdb.config import DEFAULT_MODEL_LOCATION
from imdb.core.data_loaders import load_data

log = logging.getLogger("imdb")


def evaluate():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data-dir", default=None, help="Directory where data is located"
    )
    parser.add_argument(
        "--data-filename",
        default=None,
        help="Joblib file where data is stored as a dataframe, with first column "
        "being text. "
        "It has preference over data_dir",
    )
    parser.add_argument(
        "--overwrite-cache",
        action="store_true",
        help="""
            If cache file does not exist has no effect. 
            If cache exists in the directory, overwrite it. 
            Useful when adding new files
            """,
    )
    parser.add_argument(
        "--model_location",
        default=DEFAULT_MODEL_LOCATION,
        help="Path where the model is located",
    )

    parsed_args = parser.parse_args()

    log.info(f"Starting evaluation")

    log.info(f"Loading data")
    data = load_data(
        parsed_args.data_filename, parsed_args.data_dir, not parsed_args.overwrite_cache
    )

    log.info(f"Loading model")
    model = joblib.load(parsed_args.model_location)

    log.info(f"Evaluating")
    model.evaluate(data)
