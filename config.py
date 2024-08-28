import os

API_ID = int(os.environ.get("API_ID", "6801006"))
API_HASH = os.environ.get("API_HASH", "f8abf7d5316ae065006b43e4a69bd66e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7462944085:AAFp3kFcvQAOPiCAMQEL-t1cKZjBBYrLY_U")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1002205761099")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "7241212729"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
