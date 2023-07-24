from sqlalchemy import Column, Boolean, Integer, String

from database import Base

class Todo(Base):
    __tablename__="tools"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complete = Column(Boolean, default=False)