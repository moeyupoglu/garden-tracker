from sqlalchemy import  Column,String,Integer,Boolean,ForeignKey,DateTime,Date
from sqlalchemy.sql.expression import null,text
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Plant(Base):
    __tablename__ = "plants"
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    type = Column(String,nullable=False)
    location = Column(String,nullable=False)
    notes = Column(String,nullable=False)
    image_path = Column(String,nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)

    







