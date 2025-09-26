from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)  # อ้างถึงตาราง user
    amount = Column(Float, nullable=False)
    type_ = Column(String(10), nullable=False)  # type_ เพราะหลบคำสงวน
    category = Column(String(100), default="ทั่วไป")
    description = Column(String(255), default="")
    date = Column(DateTime, default=datetime.now)
    payment_method = Column(String(50), default="เงินสด")
    
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)  # id สำหรับ DB
    google_id = Column(String(255), unique=True, nullable=True)  # id จาก Google
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    provider = Column(String(50), default="google")  # local, facebook, google
    date_joined = Column(DateTime, default=datetime.now)
    last_active = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    note = Column(String(255), default="")
    
    # hybird proproty
    transactions = relationship("Transaction",backref="user")
    
    @hybrid_property
    def sum_income(self):
        return sum(t.amount for t in self.transactions if t.type_ == "income")

    @hybrid_property
    def sum_expense(self):
        return sum(t.amount for t in self.transactions if t.type_ == "expense")
