from sqlite3 import Date
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import TIMESTAMP, Column,Integer, String,Boolean,DateTime,func
# from sqlalchemy.sql.schema import ForeignKey
# from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True , nullable=False)
    email = Column(String, nullable=False, unique=True)
    password= Column(String, nullable=False)
    is_verified = Column(Boolean , default=False)
    is_admin= Column( Boolean, default="false")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))



