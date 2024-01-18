import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "25377875"))
API_HASH = environ.get("API_HASH", "cf80e342be48570ca2e4c9d2c7695413")
BOT_TOKEN = environ.get("BOT_TOKEN", "6592668096:AAGjTkQdcb1ZFMWYCX0w0rnsL_aacrnNXLY")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001748572062"))
ADMINS = int(environ.get("ADMINS", "2034654684"))
DB_URI = environ.get("DB_URI", "mongodb+srv://nehal969797:nehalsingh969797@cluster0.4xsgmgm.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
