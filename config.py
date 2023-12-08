import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "29439475")) #optional
API_HASH = getenv("API_HASH", "e07fae9f03f2fb98991389b2c9e2ad30") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6646084739").split()))
OWNER_ID = int(getenv("OWNER_ID", "6646084739"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "6812674130:AAGqzNI5DuPZjD8GxUE-qmM0PTRna-rpXHY")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT", "I'm Sasha")
PM_LOGGER = getenv("PM_LOGGER", "-1002052301233")
LOG_GROUP = getenv("LOG_GROUP", "-1002052301233")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/l85zk/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BJWap1wBu0FRaUvP7bJg9Wl10oO67mm-sP9TOXYAh00ioAbxwWBycRipEki_hC5Kn8ck8QxTa-smWmKR0mquVihyRj8o6zLEBrKj_YhQXL8lQCVfhMO1pMW5pL8yWRxwFZv5vrz-i9OJVbmxwDghbxKh6mTRGfSrmwDI89_drFNKTbPaqHGQZ0u3Yq_tEUuc-m7eWjGbR52pDy1O_ulvHujG5OIweG6jdSqNNLCsyOMdbxQeE0jjyz3u5LJPo_8YjjyDFMy-No2VKyaSSw8Xp9VW8xc1UUJy6qB_46fudmLoTCDBLOWaLBBnuKRYk0555jq4Vn-MzdJeU12KJ1nQuFpKA6Khgo0=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
