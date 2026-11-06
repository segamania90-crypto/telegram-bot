from aiogram import Bot, Router
from aiogram.types import CallbackQuery

from handlers.function import download_and_send_media
from keyboards.inline_kb import quality_btn
import url_storage as storage

router = Router()

@router.callback_query(lambda cb: cb.data.startswith("format|"))
async def format_selection(callback: CallbackQuery):
    _, url_id = callback.data.split("|")
    url_id = url_id.strip()
    await callback.answer()
    kb = await quality_btn(url_id)
    await callback.message.answer("🎬 Видео сапаны таңдаңыз:", reply_markup=kb)

@router.callback_query(lambda cb: cb.data.startswith("video_"))
async def quality_selection(callback: CallbackQuery, bot: Bot):
    storage.url_storage = storage.load_url_storage()
    parts = callback.data.split("|")
    action = parts[0]
    url_id = parts[1].strip()
    url = storage.url_storage.get(url_id)

    if not url:
        await callback.answer("Қате: URL табылмады!")
        return

    quality = action.split("_")[1]  # 360, 480, 720, 1080
    await callback.answer("Расталды!")
    await callback.message.answer("⏳ Жүктелуде...")
    await download_and_send_media(bot, callback.message.chat.id, url, media_type='video', quality=quality)

@router.callback_query(lambda cb: cb.data.startswith("audio|"))
async def audio_selection(callback: CallbackQuery, bot: Bot):
    storage.url_storage = storage.load_url_storage()
    _, url_id = callback.data.split("|")
    url_id = url_id.strip()
    url = storage.url_storage.get(url_id)

    if not url:
        await callback.answer("Қате: URL табылмады!")
        return

    await callback.answer("Расталды!")
    await callback.message.answer("⏳ Жүктелуде...")
    await download_and_send_media(bot, callback.message.chat.id, url, media_type='audio', quality=None)