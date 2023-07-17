import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

CACHE_TIME = 10 * 5