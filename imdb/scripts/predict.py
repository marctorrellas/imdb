import argparse
import logging

import joblib
import pandas as pd

from imdb.config import DEFAULT_MODEL_LOCATION, DEFAULT_PREDICTION_LOCATION
from imdb.core.data_loaders import load_data

log = logging.getLogger("imdb")


def predict():

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
        "--model-location",
        default=DEFAULT_MODEL_LOCATION,
        help="Path where the model is located",
    )
    parser.add_argument(
        "--output-csv",
        default=DEFAULT_PREDICTION_LOCATION,
        help="Path where the resulting csv containing the predictions is dumped",
    )
    parsed_args = parser.parse_args()

    log.info("Starting prediction")

    log.info(f"Loading data")
    data = load_data(parsed_args.data_filename, parsed_args.data_dir, labelled=False)

    log.info(f"Loading model")
    model = joblib.load(parsed_args.model_location)

    log.info(f"Predicting")
    predictions = pd.DataFrame(model.predict(data.text), index=data.index)
    predictions.to_csv(parsed_args.output_csv)
    log.info(f"Predictions saved to {parsed_args.output_csv}")
