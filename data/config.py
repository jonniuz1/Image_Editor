# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# API_TOKEN = env.str("API_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
# CHANNELS = [-1001784807651]
# DB_USER = env.str("DB_USER")
# DB_PASS = env.str("DB_PASS")
# DB_NAME = env.list("DB_NAME")
# DB_HOST = env.str("DB_HOST")

"""

ADMINS: 1024717338,1684577809
API_TOKEN: 5da28da5-7d1b-4f29-b11d-cfb7421d056d
BOT_TOKEN: 5030534231:AAEE4DvzXGPka6zX87PVSZSYL_l8G-E4He4
CHANNELS: -1001784807651
"""

import os

CHANNELS = list(map(int, (str(os.environ["CHANNELS"])).split(',')))
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = list(map(int, (str(os.environ["ADMINS"])).split(',')))
IP = str(os.environ.get("ip"))
API_TOKEN = str(os.environ.get("API_TOKEN"))
