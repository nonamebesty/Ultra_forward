import datetime
from os import environ 

class Config:
    API_ID = environ.get("API_ID", "1923471")
    API_HASH = environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Forward-Bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://mvideo:mvideo@cluster0.bpj54.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Forward")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '880087645').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002396553917'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "@Egmore_links") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
