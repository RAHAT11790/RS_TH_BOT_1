# 🚀 Auto Thumbnail Telegram Bot (Pyrogram + Flask, Render-Ready)

একদম অটো-থাম্বনেইল বট —  
▶ আগে একটি ছবি পাঠান (thumbnail)  
▶ তারপর ভিডিও পাঠান  
▶ বট নতুন থাম্বসহ ভিডিও ফেরত পাঠাবে  
▶ কোনো কমান্ডের দরকার নেই 🟢

এটি Render.com-এ 24/7 রান করার জন্য সম্পূর্ণ অপটিমাইজ করা হয়েছে  
(Flask keep-alive + Pyrogram fast engine)

---

## ⭐ Features

✔ 2GB পর্যন্ত ভিডিও সাপোর্ট  
✔ Thumbnail Auto Save / Apply  
✔ Original Caption Keep  
✔ Correct Duration (00:00 বাগ নেই)  
✔ Smooth Download + Upload Progress  
✔ Render Free Tier Sleep Prevention (Flask)  
✔ কোনও Database লাগে না  
✔ Fastest possible speed (Pyrogram + TgCrypto)

---

## 🔧 Project Structure

project/ ├── bot.py ├── web.py ├── config.py ├── requirements.txt └── render.yaml   (optional)

---

## 🔌 Installation (Local)

```bash
pip install -r requirements.txt
python bot.py


---

⚙️ Configuration (config.py)

API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "123456:ABCDEF"

অথবা Render Environment Variables এ সেট করুন।


---

🚀 Deploy to Render.com

1️⃣ Repo আপলোড করুন GitHub এ

2️⃣ Render → New → Web Service

3️⃣ Build Command:

pip install -r requirements.txt

4️⃣ Start Command:

python bot.py

5️⃣ Environment Variables সেট করুন:

KEY	VALUE

API_ID	Your API ID
API_HASH	Your API Hash
BOT_TOKEN	Bot Token


6️⃣ Deploy চাপুন

Render এখন Flask সার্ভার ping করবে →
Bot আর কখনো Sleep হবে না 🔥


---

🧠 Bot Usage

📸 Step 1 — একটি ছবি পাঠান

➡ Bot এটাকে thumbnail হিসেবে সেভ করবে

🎥 Step 2 — যেকোনো ভিডিও পাঠান

➡ Bot ভিডিওটি ডাউনলোড করবে
➡ থাম্বনেইল অ্যাপ্লাই করবে
➡ সঠিক duration সেট করবে
➡ Caption 그대로 রাখবে
➡ তারপর আপনার কাছে রি-আপলোড করবে


---

📊 Progress Example

📥 Downloading:
■■■■■□□□□□ 52%
Speed: 6.2MB/s
ETA: 4 sec
32MB / 61MB

📤 Uploading:
■■■■■■■■□□ 80%
Speed: 8.1MB/s
ETA: 2 sec
50MB / 61MB


---

🔥 Tech Stack

Pyrogram v2

TgCrypto (speed boost)

Flask (Render keep-alive)

Gunicorn

Aiofiles (fast I/O)



---

🛠️ Render Sleep Prevention (Important)

Render Free Plan 15 মিনিট idle হলে Sleep mode চালু হয়।
এটি বন্ধ করতে আমরা Flask Web Server যোগ করেছি।

Render Flask server কে ping করে রাখে →
Bot 24/7 online থাকে ❤️
