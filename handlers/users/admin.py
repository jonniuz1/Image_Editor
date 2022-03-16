import asyncio
from aiogram.dispatcher import FSMContext
from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
from states.for_ads import Ad


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    count = db.count_users()[0]
    await message.answer(f"{count} ta obunachi bor!")


@dp.message_handler(text="/reklama", user_id=ADMINS, state=None)
async def start(msg: types.Message):
    await msg.reply("Reklamani kiriting:")
    await Ad.ad.set()

@dp.message_handler(state=Ad.ad)
async def send_ad_to_all(msg: types.Message, state: FSMContext):
    ads = msg.text
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=ads, disable_web_page_preview=True)
        await asyncio.sleep(0.05)
    await state.finish()
    await msg.reply("Reklama muvaffaqiyatli jo'natildi")


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
