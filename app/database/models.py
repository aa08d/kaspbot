from datetime import date

from uuid6 import uuid7
from sqlalchemy import Column, UUID, String, Date, Numeric, BigInteger
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    first_name = Column(String(150))
    last_name = Column(String(150), nullable=True)
    phone = Column(String(15), unique=True)
    code = Column(String(15), unique=True)

    documents = relationship("Document", back_populates="user", cascade="all, delete-orphan")
    consumptions = relationship("Consumption", back_populates="user", cascade="all, delete-orphan")
    telegrams = relationship("TelegramAccount", back_populates="user", cascade="all, delete-orphan")


class Consumption(Base):
    __tablename__ = "consumptions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    readings = Column(Numeric(precision=10, scale=2), nullable=False)
    photo_url = Column(String(255), nullable=False)
    date = Column(Date, default=date.today)

    user = relationship("User", back_populates="consumptions")


class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    date = Column(Date, default=date.today)

    user = relationship("User", back_populates="documents")


class TelegramAccount(Base):
    __tablename__ = "telegram_auths"

    telegram_id = Column(BigInteger, primary_key=True)

    user = relationship("User", back_populates="telegrams")
