# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "26993113"))
API_HASH = getenv("API_HASH", "bea8bb154b07fc50ee3e308772f4366c")
BOT_TOKEN = getenv("BOT_TOKEN", "7583438462:AAG2_JdQru2t7FsNtbkSVE5HLdItk8Al5-Y")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002285587854"))
