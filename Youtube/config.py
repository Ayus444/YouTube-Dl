import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7613437933:AAGTvv3LDw4KKIlzQHmQKYSdvfqSFYoEOZw")
    API_ID = int(os.environ.get("API_ID", 22581733))
    API_HASH = os.environ.get("API_HASH", "1db7bdcf908100cc641c6a5276765c3d")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/+s5fU9MLM4s80NmI1")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
