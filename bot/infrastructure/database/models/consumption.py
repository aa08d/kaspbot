from uuid6 import uuid7
from sqlalchemy import Column, UUID, Float, Date, String

from .base import Base


class Consumption(Base):
    __tablename__ = 'consumptions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    previous = Column(Float(asdecimal=True))
    current = Column(Float(asdecimal=True), nullable=True)
    photo_url = Column(String(255), nullable=True)
    date = Column(Date)
