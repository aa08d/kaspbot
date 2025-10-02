from uuid6 import uuid7
from sqlalchemy import Column, UUID, Date

from .base import Base


class Document(Base):
    __tablename__ = 'documents'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    date = Column(Date)

    user_id = Column(UUID(as_uuid=True))
