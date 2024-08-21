# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27868202"))
API_HASH = getenv("API_HASH", "bf6d423ddc4a4999f09750872bdc2497")
BOT_TOKEN = getenv("BOT_TOKEN", "7518404899:AAGgImrF37JrNTe9hWTIaOZPFjkyprCJVbc")
OWNER_ID = int(getenv("OWNER_ID", "6939667447"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://adultverse04:adultverse04@adultverse04.wpltj.mongodb.net/?retryWrites=true&w=majority&appName=adultverse04")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002234939783"))
FORCESUB = getenv("FORCESUB", "0")
