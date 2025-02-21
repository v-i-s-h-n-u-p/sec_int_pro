import os
import logging
import torch

# Model Path
MODEL_PATH = "./models/flan-alpaca-gpt4-xl"

# Sector Data Path
SECTOR_DATA_PATH = r"D:\DS\sec_pro\sectors.json"

# Logging Setup
LOG_DIR = "app/logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# Device Configuration
DEVICE = 0 if torch.cuda.is_available() else -1
