from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from .create_db import db_path


_SQLALCHEMY_DATABASE_URL = f'sqlite+aiosqlite:///{db_path}'
_engine = create_async_engine(_SQLALCHEMY_DATABASE_URL, echo=True)
async_session = async_sessionmaker(bind=_engine, class_=AsyncSession, expire_on_commit=False)
