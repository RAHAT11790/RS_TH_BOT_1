import os
import time
import math
from uuid import uuid4
from threading import Thread

from flask import Flask
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# ---------------------------
# Run Flask in Background
# ---------------------------
api = Flask(__name__)

@api.route("/")
def home():
    return "Bot Active"

def run_flask():
    api.run(host="0.0.0.0", port=10000)

Thread(target=run_flask).start()


# ---------------------------
# Pyrogram Bot
# ---------------------------
app = Client(
    "render_pyrogram_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50
)

THUMB_DIR = "thumbs"
os.makedirs(THUMB_DIR, exist_ok=True)


def get_thumb(user_id):
    path = f"{THUMB_DIR}/{user_id}.jpg"
    return path if os.path.exists(path) else None


def human(size):
    for unit in ["B","KB","MB","GB"]:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024
    return f"{size:.2f}TB"


last_edit = 0
def progress(current, total, message, start_time, prefix=""):
    global last_edit
    now = time.time()
    if now - last_edit < 1:
        return
    last_edit = now

    elapsed = now - start_time
    speed = current / elapsed if elapsed else 0
    eta = (total - current) / speed if speed else 0
    percent = (current / total) * 100

    bar = "■" * int(percent/10) + "□" * (10 - int(percent/10))

    text = (
        f"{prefix}{bar} {percent:.2f}%\n"
        f"Speed: {human(speed)}/s\n"
        f"ETA: {int(eta)} sec\n"
        f"{human(current)} / {human(total)}"
    )

    try:
        message.edit(text)
    except:
        pass


@app.on_message(filters.command("start") & filters.private)
async def start_cmd(_, m):
    me = await app.get_me()
    await m.reply_text(
        f"👋 আমি @{me.username}\n"
        "📸 আগে থাম্ব পাঠান\n"
        "🎥 তারপর ভিডিও পাঠান\n"
        "⚡ আমি থাম্বসহ ভিডিও ফেরত দেব।"
    )


@app.on_message(filters.photo & filters.private)
async def save_thumb(_, m):
    path = f"{THUMB_DIR}/{m.from_user.id}.jpg"
    await m.download(path)
    await m.reply_text("✔ থাম্বনেইল সেভ হয়েছে। এখন ভিডিও পাঠান।")


@app.on_message((filters.video | filters.document) & filters.private)
async def handle_video(_, m):
    user_id = m.from_user.id
    thumb = get_thumb(user_id)

    if not thumb:
        return await m.reply_text("❗ প্রথমে থাম্ব পাঠান।")

    caption = m.caption or ""
    duration = m.video.duration if m.video else 0

    status = await m.reply_text("📥 ডাউনলোড হচ্ছে...")

    start = time.time()
    file_path = await m.download(
        progress=lambda c,t: progress(c,t,status,start,"📥 Downloading: ")
    )

    await status.edit("📤 আপলোড হচ্ছে...")
    start = time.time()

    if m.video:
        await app.send_video(
            chat_id=m.chat.id,
            video=file_path,
            caption=caption,
            duration=duration,
            thumb=thumb,
            supports_streaming=True,
            progress=lambda c,t: progress(c,t,status,start,"📤 Uploading: ")
        )
    else:
        await app.send_document(
            chat_id=m.chat.id,
            document=file_path,
            caption=caption,
            thumb=thumb,
            progress=lambda c,t: progress(c,t,status,start,"📤 Uploading: ")
        )

    await status.edit("✔ থাম্বসহ ভিডিও পাঠানো হয়েছে!")
    os.remove(file_path)


print("🚀 Pyrogram + Flask Bot Running…")
app.run()
