import json
from config import SECTOR_DATA_PATH, logger
from model_loader import alpaca_model

# Load sector data
try:
    with open(SECTOR_DATA_PATH, "r") as file:
        sector_data = json.load(file)
except Exception as e:
    logger.error(f"Error loading sector data: {e}")
    sector_data = {"sectors": []}

def find_sector(input_text):
    """
    Matches the input text with known sector keywords.
    """
    try:
        input_text = input_text.lower()
        for sector_item in sector_data["sectors"]:
            sector = sector_item["sector"]
            keywords = sector_item["keywords"]
            for keyword in keywords:
                if keyword in input_text:
                    return sector
        return "Unknown"
    except Exception as e:
        logger.error(f"Error finding sector: {e}")
        return "Error"

def classify_sector_with_alpaca(content):
    """
    Classifies the sector of an API call using the Alpaca model.
    """
    try:
        prompt = f"Given the following API call content:\n{content}\nWhich sector does this belong to from the following list in one word?"
        response = alpaca_model(prompt, max_length=128, do_sample=True)
        value = response[0]["generated_text"].strip()
        sector = find_sector(value)
        return sector
    except Exception as e:
        logger.error(f"Error classifying sector: {e}")
        return "Error"

def detect_intent(content):
    """
    Detects the intent of an API call using the Alpaca model.
    """
    try:
        prompt = f"Consider this API call:\n{content}\nQuestion: What is the goal of this API call? for example: The goal of this API call is to retrieve booking details for a specific booking ID using a GET method. Give me the answer alone"
        intent = alpaca_model(prompt, max_length=128, do_sample=True)
        return intent[0]["generated_text"].strip()
    except Exception as e:
        logger.error(f"Error detecting intent: {e}")
        return "Error"
