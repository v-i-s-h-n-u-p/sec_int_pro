from fastapi import FastAPI, Request
from utils import classify_sector_with_alpaca, detect_intent
from config import logger

app = FastAPI()

@app.post("/sector")
async def get_sector(request: Request):
    try:
        content = await request.json()
        logger.info(f"Received API request: {content}")

        sector = classify_sector_with_alpaca(str(content))
        intent = detect_intent(str(content))

        response = {"sector": sector, "intent": intent}
        logger.info(f"Response: {response}")

        return response
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return {"error": "Internal Server Error"}
