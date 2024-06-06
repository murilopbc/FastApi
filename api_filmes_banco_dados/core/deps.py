from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

# Abrir e fechar sessão no banco

async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()
    try:
        yield session
    
    finally:
        await session.close()