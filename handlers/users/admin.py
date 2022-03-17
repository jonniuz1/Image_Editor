import asyncio
from aiogram.dispatcher import FSMContext
from aiogram import types

from data.config import ADMINS, CHANNELS
from loader import dp, db, bot
from states.for_ads import Ad
from utils.photograph import photo_link

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    count = db.count_users()[0]
    await message.answer(f"{count} ta obunachi bor!")



@dp.message_handler(text="/reklama", user_id=ADMINS, state=None)
async def start(msg: types.Message):
    await msg.reply("Reklamani kiriting:")
    await Ad.ad.set()


@dp.message_handler(state=Ad.ad, content_types=types.ContentType.PHOTO)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    msg = message.caption
    photo = message.photo[-1]
    url = await photo_link(photo)
    for user in users:
        user_id = user[0]
        await bot.send_photo(chat_id=user_id, photo=url, caption=msg)
        await asyncio.sleep(0.05)
    await bot.send_photo(chat_id=CHANNELS[-1], photo=url, caption=msg)
    await state.finish()
    await message.reply("Reklama muvaffaqiyatli jo'natildi")


@dp.message_handler(state=Ad.ad, content_types=types.ContentType.VIDEO)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    msg = message.caption
    video = message.video
    url = await photo_link(video)
    for user in users:
        user_id = user[0]
        await bot.send_video(chat_id=user_id, video=url, caption=msg)
        await asyncio.sleep(0.05)
    await bot.send_video(chat_id=CHANNELS[-1], video=url, caption=msg)
    await state.finish()
    await message.reply("Reklama muvaffaqiyatli jo'natildi")


@dp.message_handler(state=Ad.ad, content_types=types.ContentType.TEXT)
async def send_ad_to_all(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    msg = message.text
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=msg)
        await asyncio.sleep(0.05)
    await bot.send_message(chat_id=CHANNELS[-1], text=msg, disable_web_page_preview=True)
    await state.finish()
    await message.reply("Reklama muvaffaqiyatli jo'natildi")


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
