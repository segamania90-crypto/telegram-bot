import asyncio
import os
import hashlib
import yt_dlp
import time
import threading
from aiogram.types import FSInputFile
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.network import ConnectionTcpFull
from dotenv import load_dotenv

load_dotenv()

AIOGRAM_LIMIT = 50 * 1024 * 1024

API_ID = int(os.getenv('API_ID', '0'))
API_HASH = os.getenv('API_HASH')
SESSION_STRING = os.getenv('SESSION_STRING', '')

def generate_url_id(url: str):
    return hashlib.md5(url.encode()).hexdigest()

def run_telethon_in_thread(chat_id, filename, caption):
    result = {'success': False, 'error': None}

    def thread_func():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        async def send():
            client = TelegramClient(
                StringSession(SESSION_STRING),
                API_ID,
                API_HASH,
                connection=ConnectionTcpFull,
                connection_retries=10,
                retry_delay=3,
                timeout=600,
                request_retries=10,
                receive_updates=False
            )
            try:
                await client.connect()
                await client.send_file(
                    chat_id,
                    filename,
                    caption=caption,
                    supports_streaming=True,
                    part_size_kb=256
                )
                result['success'] = True
            except Exception as e:
                result['error'] = str(e)
            finally:
                try:
                    await client.disconnect()
                except:
                    pass

        loop.run_until_complete(send())
        loop.close()

    t = threading.Thread(target=thread_func)
    t.start()
    t.join(timeout=600)

    if not t.is_alive() and not result['success'] and not result['error']:
        result['success'] = True

    return result

async def send_via_telethon(chat_id: int, filename: str, media_type: str, elapsed_time: float, bot):
    print(f"Отправляю в chat_id: {chat_id}")
    caption = f"{'Міне видео' if media_type == 'video' else 'Міне аудио'}! Жүктелу уақыты {elapsed_time:.2f} секунд."

    try:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            run_telethon_in_thread,
            chat_id, filename, caption
        )

        if result['success']:
            print("Файл отправлен!")
            await bot.send_message(chat_id, "✅ Видео жіберілді!")
        else:
            error_msg = result['error'] or "Белгісіз қате"
            print(f"Telethon қате: {error_msg}")
            await bot.send_message(chat_id, f"Қате: {error_msg}")
    except Exception as e:
        print(f"Қате: {e}")
        await bot.send_message(chat_id, f"Қате: {e}")
    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass

async def download_and_send_media(bot, chat_id, url, media_type, quality=None):
    if media_type == 'video':
        if quality == '360':
            fmt = 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360][ext=mp4]/best[height<=360]/best'
        elif quality == '480':
            fmt = 'bestvideo[height<=480][ext=mp4]+bestaudio[ext=m4a]/best[height<=480][ext=mp4]/best[height<=480]/best'
        elif quality == '720':
            fmt = 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best[height<=720]/best'
        elif quality == '1080':
            fmt = 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best[height<=1080]/best'
        else:
            fmt = 'best[ext=mp4]/best'
    else:
        fmt = 'bestaudio/best'

    # ydl_opts теперь на правильном уровне отступов
    ydl_opts = {
        'format': fmt,
        'outtmpl': f'downloads/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': False,
        'merge_output_format': 'mp4',
        'ffmpeg_location': r'C:\Users\ERJAN\Desktop\PYTHON\bot tel',
    }

    filename = None
    try:
        start_time = time.time()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            if not filename.endswith('.mp4') and media_type == 'video':
                filename = os.path.splitext(filename)[0] + '.mp4'

        elapsed_time = time.time() - start_time
        filesize = os.path.getsize(filename)

        if filesize > AIOGRAM_LIMIT:
            size_mb = filesize / (1024 * 1024)
            await bot.send_message(chat_id, f"📦 Файл {size_mb:.1f} МБ — Қазір видеоны жіберемін...")
            await send_via_telethon(chat_id, filename, media_type, elapsed_time, bot)
        else:
            media_file = FSInputFile(filename)
            caption = f"{'Міне видео' if media_type == 'video' else 'Міне аудио'}! Жүктелу уақыты {elapsed_time:.2f} секунд."
            if media_type == "video":
                await bot.send_video(chat_id, media_file, caption=caption, request_timeout=300)
            else:
                await bot.send_audio(chat_id, media_file, caption=caption, request_timeout=300)

            await asyncio.sleep(1)
            if os.path.exists(filename):
                os.remove(filename)

    except Exception as e:
        await asyncio.sleep(1)
        if filename and os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass
        await bot.send_message(chat_id, f"Қате: {e}")