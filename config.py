from os import environ

API_ID = int(environ.get("API_ID", "29031294"))
API_HASH = environ.get("API_HASH", "125aaa467af268e97314e055ba3d56b6")
BOT_TOKEN = environ.get("BOT_TOKEN", "7983985478:AAEhK_R0pIgsQZJ8dlCnROc6h7VsE1_CLGY")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002427686991"))
ADMINS = int(environ.get("ADMINS", "7535513082"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://join:join@cluster0.ojdfgdu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "join")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
