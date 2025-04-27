import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Secret key (sk_live_xxx) loaded securely
API_KEY = os.getenv('SECRET_API_KEY')

# Bank or Payment API endpoint (example)
BLOCK_CARD_ENDPOINT = "https://api.bankservice.com/v1/cards/block"

# Card you want to block
CARD_ID = "card_123456789"

def block_card(card_id):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "card_id": card_id,
        "reason": "lost"   # Other reasons: "stolen", "fraud", etc.
    }
    
    try:
        response = requests.post(BLOCK_CARD_ENDPOINT, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"✅ Card {card_id} successfully blocked!")
        else:
            print(f"❌ Failed to block card. Status: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"⚠️ Error occurred: {str(e)}")

if __name__ == "__main__":
    if API_KEY is None:
        print("🚫 Error: API key is missing! Check your .env file.")
    else:
        block_card(CARD_ID)
