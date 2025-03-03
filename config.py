import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

SITES_TO_MONITOR = [
    "http://hacked-data.onion",
    "http://breach-forums.onion"
]


EMAIL_CONFIG = {
    "sender": os.getenv("sender email"),
    "password": os.getenv("app password"),
    "receiver": os.getenv("receiver email")
}

DATABASE_FILE = "data/leaked_data.db"
