# 🤖 Telegram Media Downloader Bot

---

## 🇰🇿 Қазақша

YouTube және TikTok-тан видео және аудио жүктейтін Telegram боты. ДК-да жергілікті түрде іске қосылады.

### ⚙️ Не істей алады
- **YouTube** және **TikTok** сілтемесі арқылы видео жүктейді
- Видео сапасын таңдау: **360p, 480p, 720p, 1080p**
- Видеодан **аудио** (mp3) жүктейді
- Файлды чатқа автоматты түрде жібереді
- 50 МБ-тан үлкен файлдарды Telethon арқылы шектеусіз жібереді

### 📦 Орнату
```bash
git clone https://github.com/segamania90-crypto/telegram-bot.git
cd telegram-bot
python -m venv venv
venv\Scripts\activate
pip install aiogram telethon yt-dlp python-dotenv
```

### `.env` файлын жасаңыз
```
BOT_TOKEN=BotFather_токені
```

### 🚀 Іске қосу
```bash
python bot_telegram.py
```

### 💬 Қалай пайдалану керек
1. Ботқа `/start` жаз
2. YouTube немесе TikTok сілтемесін жібер
3. Форматты таңда: **Видео** немесе **Аудио**
4. Видео үшін сапаны таңда: 360p / 480p / 720p / 1080p
5. Жүктелуді күт — бот файлды жібереді

---

## 🇷🇺 Русский

Телеграм-бот для скачивания видео и аудио с YouTube и TikTok. Запускается локально на ПК.

### ⚙️ Что умеет
- Скачивает видео с **YouTube** и **TikTok** по ссылке
- Выбор качества видео: **360p, 480p, 720p, 1080p**
- Скачивает **аудио** (mp3) из видео
- Автоматически отправляет файл в чат
- Большие файлы (>50 МБ) отправляет через Telethon без ограничений

### 📦 Установка
```bash
git clone https://github.com/segamania90-crypto/telegram-bot.git
cd telegram-bot
python -m venv venv
venv\Scripts\activate
pip install aiogram telethon yt-dlp python-dotenv
```

### `.env` файл
```
BOT_TOKEN=твой_токен_от_BotFather
```

### 🚀 Запуск
```bash
python bot_telegram.py
```

### 💬 Как пользоваться
1. Напиши боту `/start`
2. Отправь ссылку на YouTube или TikTok видео
3. Выбери формат: **Видео** или **Аудио**
4. Для видео выбери качество: 360p / 480p / 720p / 1080p
5. Дождись загрузки — бот пришлёт файл

---

## 🇬🇧 English

A Telegram bot for downloading video and audio from YouTube and TikTok. Runs locally on your PC.

### ⚙️ Features
- Download videos from **YouTube** and **TikTok** by link
- Choose video quality: **360p, 480p, 720p, 1080p**
- Extract **audio** (mp3) from videos
- Automatically sends the file to the chat
- Files larger than 50 MB are sent via Telethon without size limits

### 📦 Installation
```bash
git clone https://github.com/segamania90-crypto/telegram-bot.git
cd telegram-bot
python -m venv venv
venv\Scripts\activate
pip install aiogram telethon yt-dlp python-dotenv
```

### `.env` file
```
BOT_TOKEN=your_token_from_BotFather
```

### 🚀 Run
```bash
python bot_telegram.py
```

### 💬 How to use
1. Send `/start` to the bot
2. Send a YouTube or TikTok link
3. Choose format: **Video** or **Audio**
4. For video, choose quality: 360p / 480p / 720p / 1080p
5. Wait for the download — the bot will send you the file

---

## 📁 Project Structure / Структура / Құрылым

```
├── handlers/
│   ├── callback.py     # Button handlers (format and quality selection)
│   ├── commands.py     # Bot commands (/start, link handling)
│   └── function.py     # Download and send media
├── keyboards/
│   └── inline_kb.py    # Inline buttons for format/quality
├── bot_telegram.py     # Main entry point
├── url_storage.py      # URL storage between steps
├── .env                # Secret keys (never upload to GitHub!)
└── .gitignore
```

## 🛠️ Tech Stack
- [Aiogram 3](https://docs.aiogram.dev/) — Telegram bot framework
- [Telethon](https://docs.telethon.dev/) — for sending large files
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — video downloading
- [FFmpeg](https://ffmpeg.org/) — video processing

## ⚠️ Important / Важно / Маңызды

- 🔐 Never upload your `.env` file to GitHub / Никогда не загружай `.env` на GitHub / `.env` файлын GitHub-қа жүктемеңіз
- 💻 The bot only works while running on your PC / Бот работает только пока запущен на ПК / Бот тек ДК іске қосылғанда жұмыс істейді
