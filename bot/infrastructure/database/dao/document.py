from uuid import UUID
from datetime import date

from sqlalchemy import select, extract
from sqlalchemy.ext.asyncio import AsyncSession

from bot.infrastructure.database.models import Document


class DocumentDAO:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, document_id: UUID) -> Document:
        stmt = select(Document).filter(Document.id == document_id)
        result = await self.session.execute(stmt)
        document = result.scalars().first()
        return document

    async def get_user_document_by_period(self, user_id: UUID, month: int, year: int) -> Document:
        stmt = select(Document).filter(
            Document.user_id == user_id,
            extract("month", Document.date) == month,
            extract("year", Document.date) == year,
        )
        document = await self.session.execute(stmt)
        return document.scalar_one_or_none()

    async def create(self, user_id: UUID) -> Document:
        document = Document(
            user_id=user_id,
            date=date.today()
        )
        self.session.add(document)
        await self.session.commit()
        return document
