from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", "8675734de0e638e63cb0e093a045644d")
BOT_TOKEN = getenv("BOT_TOKEN", "5832136580:AAH_qxzJCy362gXKsouiiOaoUNQIbPZ8eVY")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
