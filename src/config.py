import logging
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format="%(asctime)s - %(name)s - %(message)s",
)
logger = logging.getLogger("imdb")
