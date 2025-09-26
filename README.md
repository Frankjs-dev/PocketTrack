📌 PocketTrack – แอปรายรับรายจ่ายออนไลน์

PocketTrack คือเว็บแอปสำหรับบันทึกรายรับ–รายจ่าย ใช้งานง่าย ปลอดภัย และสามารถเข้าถึงได้จากทุกที่ พัฒนาด้วย Flask และ SQLAlchemy พร้อมระบบล็อกอินด้วย Authlib และรองรับการ Deploy บน Render ด้วย Gunicorn

✨ ฟีเจอร์หลัก

บันทึก รายรับ–รายจ่าย ได้อย่างรวดเร็ว

ดูยอดรวม คงเหลือ (Balance) แบบเรียลไทม์

ระบบ ล็อกอินปลอดภัย ด้วย OAuth (Authlib)

จัดเก็บข้อมูลด้วย SQLAlchemy ORM (รองรับ SQLite / PostgreSQL)

พร้อมใช้งานจริงบน Render ด้วย Gunicorn

🛠️ เทคโนโลยีที่ใช้

Backend: Flask

Database: SQLAlchemy

Authentication: Authlib (OAuth 2.0)

Production Server: Gunicorn

Deployment: Render

🚀 วิธีติดตั้งและใช้งาน

โคลนโปรเจกต์

git clone https://github.com/USERNAME/PocketTrack.git
cd PocketTrack


สร้าง Virtual Environment และติดตั้ง dependencies

python -m venv venv
venv\Scripts\activate   # สำหรับ Windows
source venv/bin/activate # สำหรับ Mac/Linux

pip install -r requirements.txt


ตั้งค่า Env (.env)

FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3


รันเซิร์ฟเวอร์ในเครื่อง

flask run


Deploy ขึ้น Render

ใช้ Gunicorn เป็น WSGI server

เชื่อมต่อกับ Database (PostgreSQL แนะนำสำหรับ production)

📄 License

โครงการนี้เผยแพร่ภายใต้ MIT License
