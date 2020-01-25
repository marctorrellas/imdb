from _datetime import datetime
import logging
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_DATA_LOCATION = PROJECT_DIR / "data/sample/"
DEFAULT_SUBSAMPLE = 100
date = datetime.now().strftime("%Y_%m_%d")
DEFAULT_MODEL_LOCATION = f"model_{date}.joblib"
DEFAULT_PREDICTION_LOCATION = f"predictions_{date}.csv"
# centralised value for all random seeds
RANDOM_STATE = 8
CV_TRAIN_SIZE = 0.6

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="%(asctime)s - %(name)s - %(message)s",
)
logger = logging.getLogger("imdb")
