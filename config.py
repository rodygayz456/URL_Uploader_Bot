import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "5859491010:AAHdjkcotSxo2CglZ-c_jD5uk_uMOsvBgAo") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 26607105)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "ca6186c6553ffe7db21f8f0b67765337") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1287792972")) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://umar786:umar786@cluster0.rpuio0h.mongodb.net/?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
