from transformers import pipeline
from huggingface_hub import snapshot_download
from config import MODEL_PATH, DEVICE, logger

def download_model():
    try:
        logger.info("Downloading model...")
        snapshot_download(repo_id="declare-lab/flan-alpaca-gpt4-xl", local_dir=MODEL_PATH)
        logger.info("Model downloaded successfully.")
    except Exception as e:
        logger.error(f"Error downloading model: {e}")

def load_model():
    try:
        logger.info("Loading model...")
        model = pipeline("text2text-generation", model=MODEL_PATH, device=DEVICE)  # Explicit task
        logger.info("Model loaded successfully.")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

# Ensure model is downloaded before usage
download_model()
alpaca_model = load_model()
