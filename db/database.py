import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from db.models import Base

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)


# แก้ไข URL สำหรับ Postgres
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')

engine = create_engine(DATABASE_URL)

# ให้ SQLAlchemy เช็กและสร้างตารางใหม่ที่ยังไม่มี
Base.metadata.create_all(engine)
