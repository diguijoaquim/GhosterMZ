import sqlalchemy
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,Integer,DateTime

Base=declarative_base()
class Ataque(Base):
    __tablename__="ataques"
    id=Column(Integer,primary_key=True)
    ip=Column(String(20))
    latitude=Column(String(20))
    longitude=Column(String(20))
    type=Column(String(50))
    username=Column(String(100))
    password=Column(String(100))
    datetime=Column(DateTime)