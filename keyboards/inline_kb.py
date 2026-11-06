from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def format_btn(url_id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎬 Видео", callback_data=f"format|{url_id}")],
        [InlineKeyboardButton(text="🎵 Аудио", callback_data=f"audio|{url_id}")]
    ])
    return keyboard

async def quality_btn(url_id):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📱 360p", callback_data=f"video_360|{url_id}")],
        [InlineKeyboardButton(text="📺 480p", callback_data=f"video_480|{url_id}")],
        [InlineKeyboardButton(text="🖥 720p", callback_data=f"video_720|{url_id}")],
        [InlineKeyboardButton(text="🎯 1080p", callback_data=f"video_1080|{url_id}")]
    ])
    return keyboard