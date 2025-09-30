from uuid6 import uuid7
from sqlalchemy import Column, UUID, String

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone = Column(String(15))
