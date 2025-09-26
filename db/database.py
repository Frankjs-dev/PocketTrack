import os
from sqlalchemy import create_engine
from db.models import Base

# ใช้ PostgreSQL URL จาก Render แทน SQLite
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///pockettrack.db')

# แก้ไข URL สำหรับ Postgres
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')

engine = create_engine(DATABASE_URL)

# ให้ SQLAlchemy เช็กและสร้างตารางใหม่ที่ยังไม่มี
Base.metadata.create_all(engine)
