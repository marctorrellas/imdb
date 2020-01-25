import argparse
import logging

import joblib

from imdb.config import DEFAULT_MODEL_LOCATION, DEFAULT_SUBSAMPLE, RANDOM_STATE
from imdb.core.data_loaders import load_data
from imdb.models.models import ClassicalModel

log = logging.getLogger("imdb")


def train():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-dir", default=None, help="Directory where data is located"
    )
    parser.add_argument(
        "--cv-enabled",
        action="store_true",
        help="If supplied, 3-fold cross-validation is carried out",
    )
    parser.add_argument(
        "--calibration-enabled",
        action="store_true",
        help="If supplied, calibration of the decision threshold is carried out",
    )
    parser.add_argument(
        "--data-filename",
        default=None,
        help="Joblib file where data is stored as a dataframe, with first column "
        "being text, and second column being the label. "
        "It has preference over data_dir",
    )
    parser.add_argument(
        "--overwrite-cache",
        action="store_true",
        help="""
        If cache file does not exist has no effect. 
        If cache exists in the directory, overwrite it. 
        Useful when adding new files to data dir.
        """,
    )
    parser.add_argument(
        "--model-location",
        default=DEFAULT_MODEL_LOCATION,
        help="Path where the model should be saved",
    )
    parser.add_argument(
        "--subsample",
        default=None,
        help="If not None, use only a random sample of the data",
    )
    parsed_args = parser.parse_args()

    log.info(f"Starting training")

    # TODO: it'd be more efficient to subsample when reading data rather than read all
    #  and then drop
    log.info("Loading all data")
    data = load_data(
        parsed_args.data_filename, parsed_args.data_dir, not parsed_args.overwrite_cache
    )

    subsample = parsed_args.subsample
    if subsample:
        n = subsample or DEFAULT_SUBSAMPLE
        log.info(f"Subsampling to get {n} samples")
        data = data.sample(n, random_state=RANDOM_STATE)

    model = ClassicalModel()
    model.train(data, parsed_args.cv_enabled, parsed_args.calibration_enabled)

    model_location = parsed_args.model_location
    joblib.dump(model, model_location)
    log.info(f"Model saved to {model_location}")
