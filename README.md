📌 PocketTrack – แอปรายรับรายจ่ายออนไลน์
จัดทำโดย นายชนายุ งามประดิษฐ์ CSS001 ภาคสมทบ

PocketTrack คือเว็บแอปสำหรับ บันทึกรายรับ–รายจ่าย ที่ใช้งานง่าย ปลอดภัย และเข้าถึงได้จากทุกที่
พัฒนาด้วย Flask + SQLAlchemy พร้อมระบบล็อกอินด้วย OAuth (Authlib) และรองรับการ Deploy บน Render ด้วย Gunicorn

🔗 เว็บไซต์ตัวอย่าง: https://pockettrack-teon.onrender.com/
<img width="779" height="1199" alt="image" src="https://github.com/user-attachments/assets/30234155-4c19-4f04-bd25-7d8e43f09505" />


✨ ฟีเจอร์หลัก

📝 บันทึกรายรับ–รายจ่าย ได้อย่างรวดเร็ว

💰 ดูยอดรวมและคงเหลือ (Balance) แบบเรียลไทม์

🔑 ระบบล็อกอินปลอดภัย ด้วย Google OAuth (Authlib)

🗄️ จัดเก็บข้อมูลด้วย SQLAlchemy ORM (รองรับ SQLite และ PostgreSQL)

🚀 รองรับ Production Deployment บน Render ด้วย Gunicorn

🛠️ เทคโนโลยีที่ใช้

Backend: Flask

Database: SQLAlchemy (SQLite / PostgreSQL)

Authentication: Authlib (OAuth 2.0)

Production Server: Gunicorn

Deployment: Render

🚀 วิธีติดตั้งและใช้งาน
1. โคลนโปรเจกต์
git clone https://github.com/USERNAME/PocketTrack.git
cd PocketTrack

2. สร้าง Virtual Environment และติดตั้ง dependencies
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt

3. ตั้งค่า Environment Variables (.env)
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3   # ใช้ SQLite สำหรับ dev, PostgreSQL สำหรับ production

4. รันเซิร์ฟเวอร์ (Local)
flask run


เข้าใช้งานที่ http://localhost:5000

5. Deploy บน Render

ใช้ Gunicorn เป็น WSGI server

ตั้งค่า DATABASE_URL เป็น PostgreSQL (Render จะให้ URL มา)

📦 requirements.txt (ตัวอย่าง)
Flask==2.3.3
Authlib==1.2.1
SQLAlchemy==2.0.39
python-dotenv==1.0.0
gunicorn==21.2.0
psycopg==3.2.3   # ถ้าใช้ PostgreSQL บน Python 3.13

📄 License

โครงการนี้เผยแพร่ภายใต้ MIT License
