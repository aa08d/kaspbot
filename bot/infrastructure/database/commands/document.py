from uuid import UUID
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import Document
from bot.infrastructure.database.dao import DocumentDAO


@dataclass(frozen=True)
class CreateDocumentCommand:
    user_id: UUID

async def create_document(command: CreateDocumentCommand, session: AsyncSession) -> Document:
    dao = DocumentDAO(session)
    document = await dao.create(user_id=command.user_id)
    return document
