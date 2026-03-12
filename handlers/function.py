import os
import hashlib
import yt_dlp
import time
from aiogram.types import FSInputFile

def generate_url_id(url: str):
    return hashlib.md5(url.encode()).hexdigest()

async def download_and_send_media(bot, chat_id, url, media_type):
    ydl_opts_info = {
        'quiet': True,
        'no_warnings': True,
    }

    try:
        # Сначала проверяем размер без скачивания
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info = ydl.extract_info(url, download=False)
            filesize = info.get('filesize') or info.get('filesize_approx') or 0

            if filesize > 50 * 1024 * 1024:  # 50MB в байтах
                size_mb = filesize / (1024 * 1024)
                await bot.send_message(
                    chat_id,
                    f"❌ Видео тым үлкен ({size_mb:.1f} MB)\n"
                    f"Максимум: 50 MB\n"
                    f"Басқа сілтеме жіберіп көріңіз 🙏"
                )
                return

        # Если размер ок — скачиваем
        ydl_opts = {
            'format': 'best[ext=mp4]/best' if media_type == 'video' else 'bestaudio/best',
            'outtmpl': f'downloads/%(title)s.{"mp4" if media_type == "video" else "m4a"}',
        }

        start_time = time.time()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        end_time = time.time()
        elapsed_time = end_time - start_time

        media_file = FSInputFile(filename)
        if media_type == "video":
            await bot.send_video(chat_id, media_file, caption=f"Міне видео! Жүктелу уақыты {elapsed_time:.2f} секунд.")
        else:
            await bot.send_audio(chat_id, media_file, caption=f"Міне аудио! Жүктелу уақыты {elapsed_time:.2f} секунд.")

        os.remove(filename)

    except Exception as e:
        await bot.send_message(chat_id, f"Қате: {e}")