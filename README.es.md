# 🤖 Telegram Media Downloader Bot

**Un bot de Telegram para descargar video y audio de YouTube y TikTok. Se ejecuta localmente en tu PC.**

[🇬🇧 English](README.md#-english) | [🇷🇺 Русский](README.md#-русский) | [🇰🇿 Қазақша](README.md#-қазақша) | [🇪🇸 Español](#-español)

---

## 🇪🇸 Español

### ⚙️ Características
- Descarga videos de **YouTube** y **TikTok** por enlace
- Elige calidad de video: **360p, 480p, 720p, 1080p**
- Extrae **audio** (mp3) de videos
- Envía automáticamente el archivo al chat
- Archivos mayores a 50 MB se envían vía Telethon sin límites

### 📦 Configuración
```bash
git clone https://github.com/segamania90-crypto/telegram-bot.git
cd telegram-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Variables de entorno
Crea un archivo `.env` basado en `.env.example`:
```
BOT_TOKEN=tu_token_de_BotFather
API_ID=tu_api_id_de_my.telegram.org
API_HASH=tu_api_hash_de_my.telegram.org
SESSION_STRING=tu_session_string_de_telethon
```

> **Nota:** `ffmpeg` debe instalarse por separado en tu sistema y estar en el PATH (o coloca `ffmpeg.exe` en la raíz del proyecto para Windows). Descarga desde [ffmpeg.org](https://ffmpeg.org/download.html).

### 🚀 Ejecutar
```bash
python bot_telegram.py
```

### 💬 Cómo usar
1. Envía `/start` al bot
2. Envía un enlace de YouTube o TikTok
3. Elige formato: **Video** o **Audio**
4. Para video, elige calidad: 360p / 480p / 720p / 1080p
5. Espera la descarga — el bot te enviará el archivo

---

## 🇬🇧 English

### ⚙️ Features
- Download videos from **YouTube** and **TikTok** by link
- Choose video quality: **360p, 480p, 720p, 1080p**
- Extract **audio** (mp3) from videos
- Automatically sends the file to the chat
- Files larger than 50 MB are sent via Telethon without size limits

### 📦 Setup
```bash
git clone https://github.com/segamania90-crypto/telegram-bot.git
cd telegram-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Required Environment Variables
Create a `.env` file based on `.env.example`:
```
BOT_TOKEN=your_token_from_BotFather
API_ID=your_api_id_from_my.telegram.org
API_HASH=your_api_hash_from_my.telegram.org
SESSION_STRING=your_telethon_session_string
```

> **Note:** `ffmpeg` must be installed separately on your system and available in PATH (or place `ffmpeg.exe` in the project root for Windows). Download from [ffmpeg.org](https://ffmpeg.org/download.html).

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

## 🇷🇺 Русский

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
pip install -r requirements.txt
```

### Переменные окружения
Создайте файл `.env` на основе `.env.example`:
```
BOT_TOKEN=твой_токен_от_BotFather
API_ID=твой_api_id_с_my.telegram.org
API_HASH=твой_api_hash_с_my.telegram.org
SESSION_STRING=твоя_telethon_сессия
```

> **Примечание:** `ffmpeg` нужно установить отдельно в системе и добавить в PATH (или положить `ffmpeg.exe` в корень проекта для Windows). Скачать с [ffmpeg.org](https://ffmpeg.org/download.html).

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

## 🇰🇿 Қазақша

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
pip install -r requirements.txt
```

### Мүлікті ортасы
`.env` файлын `.env.example` негізінде жасаңыз:
```
BOT_TOKEN=BotFather_токені
API_ID=my.telegram.org-дан_api_id
API_HASH=my.telegram.org-дан_api_hash
SESSION_STRING=telethon_сессиясы
```

> **Ескерту:** `ffmpeg` жүйеде бөлек орнатылуы керек және PATH-да болуы тиіс (немесе Windows үшін `ffmpeg.exe` файлын жобаның түбірінен қойыңыз). Жүктеу: [ffmpeg.org](https://ffmpeg.org/download.html).

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

## 📁 Estructura del Proyecto / Project Structure / Структура / Құрылым

```
├── handlers/
│   ├── callback.py     # Manejadores de botones (selección de formato y calidad)
│   ├── commands.py     # Comandos del bot (/start, manejo de enlaces)
│   └── function.py     # Descargar y enviar medios
├── keyboards/
│   └── inline_kb.py    # Botones inline para formato/calidad
├── bot_telegram.py     # Punto de entrada principal
├── url_storage.py      # Almacenamiento de URLs entre pasos
├── url_storage.json    # Almacenamiento persistente de URLs (auto-generado)
├── .env                # Claves secretas (¡nunca subas a GitHub!)
├── .env.example        # Plantilla para variables de entorno
├── requirements.txt    # Dependencias de Python
└── .gitignore
```

## 🛠️ Stack Tecnológico
- [Aiogram 3](https://docs.aiogram.dev/) — Framework para bots de Telegram
- [Telethon](https://docs.telethon.dev/) — Para enviar archivos grandes
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — Descarga de videos
- [FFmpeg](https://ffmpeg.org/) — Procesamiento de video (instalar por separado)

## ⚠️ Descargo de responsabilidad / Disclaimer / Дисклеймер / Жауапкершілік шарты

**Este es un proyecto educativo.** El usuario es el único responsable de cumplir con los Términos de Servicio de YouTube y TikTok, las leyes de derechos de autor y las políticas de uso de API. Úselo bajo su propio riesgo.

**This is an educational project.** The user is solely responsible for complying with YouTube and TikTok Terms of Service, copyright laws, and API usage policies. Use at your own risk.

**Это учебный проект.** Пользователь самостоятельно отвечает за соблюдение правил YouTube и TikTok, законов об авторском праве и политик использования API. Используйте на свой страх и риск.

**Бұл оқу жобасы.** Пайдаланушы YouTube және TikTok ережелеріне, авторлық құқық заңдарына және API пайдалану саясатына сәйкес келу үшін тек өзін-өзі жауапты. Өзіңіздің тәуекеліңізде пайдалыңыз.

---

## 🔐 Seguridad / Security / Безопасность / Қауіпсіздік

- 🔐 Nunca subas tu archivo `.env` a GitHub / Never upload your `.env` file to GitHub / Никогда не загружай `.env` на GitHub / `.env` файлын GitHub-қа жүктемеңіз
- 💻 El bot solo funciona mientras se ejecuta en tu PC / The bot only works while running on your PC / Бот работает только пока запущен на ПК / Бот тек ДК іске қосылғанда жұмыс істейді