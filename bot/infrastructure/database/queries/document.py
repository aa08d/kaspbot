from uuid import UUID
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import Document
from bot.infrastructure.database.dao import DocumentDAO


@dataclass(frozen=True)
class GetDocumentByIDQuery:
    document_id: UUID

async def get_document_by_id(
    command: GetDocumentByIDQuery,
    session: AsyncSession,
) -> Document:
    dao = DocumentDAO(session)
    document = await dao.get_by_id(command.document_id)
    return document


@dataclass(frozen=True)
class GetUserDocumentByPeriodQuery:
    user_id: UUID
    month: int
    year: int

async def get_user_document_by_period(
    command: GetUserDocumentByPeriodQuery,
    session: AsyncSession,
) -> Document:
    dao = DocumentDAO(session)
    document = await dao.get_user_document_by_period(
        user_id=command.user_id,
        month=command.month,
        year=command.year,
    )
    return document
