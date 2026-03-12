from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

import keyboards.inline_kb as in_kb 
import handlers.function as hf 
import url_storage as storage 

router = Router()

@router.message(CommandStart())  
async def cmd_start(message: Message):
    await message.reply("Салам! Yotube н/е Тик Ток-тағы видеоның сілтемесін жіберсең, мен сол видеоны жүктеуге көмектесемін!")

@router.message(lambda message: "tiktok.com" in message.text or "youtube.com" in message.text or "youtu.be" in message.text)
async def video_request(message: Message):
    url = message.text.strip()
    url_id = hf.generate_url_id(url)
    storage.url_storage[url_id] = url
    storage.save_url_storage(storage.url_storage)
    await message.answer ("Жүктеу форматын таңдаңыз:", reply_markup= await in_kb.format_btn(url_id)) 