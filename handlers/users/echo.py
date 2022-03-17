from aiogram import types

from data.config import BOT_TOKEN
from loader import dp, bot


# Echo bot
#
from utils.photograph import photo_link


@dp.message_handler(content_types=[types.ContentType.VIDEO, types.ContentType.PHOTO])
async def get_image_from_user(message: types.Message):
    msg = message.caption
    photo = message.photo[-1]
    url = await photo_link(photo)
    await bot.send_photo(chat_id=message.from_user.id, photo=url, caption=msg)
