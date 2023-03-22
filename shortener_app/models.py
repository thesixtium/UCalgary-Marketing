from sqlalchemy import Boolean, Column, Integer, String, Float

from .database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)

    title = Column(String)
    desc = Column(String)
    x = Column(Float)
    y = Column(Float)
    floor = Column(Integer)

