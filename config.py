# ---------------------------------------------------------------------

# This file is a part of https://github.com/AnonXTG/AnonX. Licenced under GNU Public Licence.

# The GNU General Public License is a free, copyleft license for
# software and other kinds of works.

# The licenses for most software and other practical works are designed
# to take away your freedom to share and change the works.  By contrast,
# the GNU General Public License is intended to guarantee your freedom to
# share and change all versions of a program--to make sure it remains free
# software for all its users.  We, the Free Software Foundation, use the
# GNU General Public License for most of our software; it applies also to
# any other work released this way by its authors.  You can apply it to
# your programs, too.

# ---------------------------------------------------------------------

import os

# Some Vars are already filled you need not to fill the again

# Token from botfather 
TOKEN = os.environ.get("TOKEN", "")

# A group ID where your logs will be stored that what is happening with your bot.
JOIN_LOGGER = os.environ.get("EVENT_LOGS", "")

# only one # don't remove other one.
OWNER_ID = int(os.environ.get("OWNER_ID", "5330301316", "fill_your_id_here_")) 

# only one # don't remove other one.
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "itz_unknown_person", "Your_username_here")

# can add multiple with spaces
DRAGONS = {int(x) for x in os.environ.get("DRAGONS", "").split()}

# can add multiple with spaces
DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "").split()}

# can add multiple with spaces
DEMONS = {int(x) for x in os.environ.get("DEMONS", "").split()} 

# can add multiple with spaces
WOLVES = {int(x) for x in os.environ.get("WOLVES", "").split()}

# can add multiple with spaces
TIGERS = {int(x) for x in os.environ.get("TIGERS", "").split()}
 
INFOPIC = bool(os.environ.get("INFOPIC", True)) or "https://te.legra.ph/file/d32e45c80e56fa1f97af1.jpg"

EVENT_LOGS = os.environ.get("EVENT_LOGS", None)

ERROR_LOGS = os.environ.get("ERROR_LOGS", None)

# Don't touch if you don't know.
WEBHOOK = bool(os.environ.get("WEBHOOK", False))

# heroku app url
URL = os.environ.get("URL", "")  # If You Deploy On Heroku. [URL PERTEN:- https://{appname}.herokuapp.com/ || EXP:- https://AnonX.herokuapp.com/]
PORT = int(os.environ.get("PORT", 8443))

CERT_PATH = os.environ.get("CERT_PATH")

# Bot Owner's API_ID (From:- https://my.telegram.org/apps)
API_ID = os.environ.get("API_ID", "")

# Bot Owner's API_HASH (From:- https://my.telegram.org/apps)
API_HASH = os.environ.get("API_HASH", "")

# Any SQL Database Link (RECOMMENDED:- PostgreSQL & https://www.elephantsql.com)
DB_URL = os.environ.get("DATABASE_URL", "") 

# Don't touch
DB_URL = DB_URL.replace(
"postgres://", "postgresql://", 1
)  # rest of connection code using the connection string `uri`

# Donation Link (ANY)
DONATION_LINK = os.environ.get("https://t.me/i_14344")

# Wall api key for wallpapers # From:- https://wall.alphacoders.com/api.php
WALL_API = os.environ.get("WALL_API", None) 

To remove background of images # From:- https://www.remove.bg/
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", "")

OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "") # From:- https://openweathermap.org/api
GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None) # From:- http://genius.com/api-clients
MONGO_DB_URL = os.environ.get("MONGO_DB_URL", True)
REDIS_URL = os.environ.get("REDIS_URL", True)
BOT_ID = int(os.environ.get("BOT_ID", None)) # Get the user ID of bot, if you are using Telegram's unofficial app, it is easy to find.
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None) # Support Chat Group Link (Use AnonXChats || Dont Use https://t.me/AnonXChats)
SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None) # Use @SpamWatchSupport
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None) # From https://t.me/SpamWatchBot 
BOT_USERNAME = os.environ.get("BOT_USERNAME", "") # Bot Username

STRING_SESSION = os.environ.get("STRING_SESSION", None) # Telethon Based String Session
REPO = "AnonXTG/AnonX "
DEVELOPER = "AnonXTG"
APP_ID = API_ID
APP_HASH = API_HASH
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", True) # Heroku App Name 
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", True) # Heroku API [From https://dashboard.heroku.com/account]
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", True)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", True)
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", True)
ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True) 
BOT_NAME = os.environ.get("BOT_NAME", True) 
MONGO_DB = "AnonX" # Don't change else errors.
ARQ_API_URL = "https://arq.hamker.in"
GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"
CHROME_DRIVER = "/usr/bin/chromedriver"
SUDO_USERS = "5033682545"
WHITELIST_USERS = "5033682545"
BOT_API_URL = os.environ.get('BOT_API_URL', "https://api.telegram.org/bot")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "TheAnonX")

HELP_IMG = os.environ.get("HELP_IMG", True) or "https://te.legra.ph/file/d32e45c80e56fa1f97af1.jpg"
GROUP_START_IMG = os.environ.get("GROUP_START_IMG", True) or "https://te.legra.ph/file/d32e45c80e56fa1f97af1.jpg"
anon_pic = os.environ.get("anon_pic", True) or "@https://te.legra.ph/file/d32e45c80e56fa1f97af1.jpg"

BL_CHATS = {int(x) for x in os.environ.get("BL_CHATS", "").split()}


# Don't Change anything if you don't know what to do here...!!!

LOAD = os.environ.get("LOAD", "").split() 

NO_LOAD = os.environ.get("NO_LOAD", "translation").split()

DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))

STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False)) or "True"

WORKERS = int(os.environ.get("WORKERS", 8))

BAN_STICKER = os.environ.get("BAN_STICKER", "")

ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)

TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")

CASH_API_KEY = os.environ.get("CASH_API_KEY", None) or "8FKSK3MXCZYUXWQ3"

TIME_API_KEY = os.environ.get("TIME_API_KEY", None) or "TWID5QWYJTAX"
