from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


_SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///database/all_school.db'
_engine = create_async_engine(_SQLALCHEMY_DATABASE_URL)
async_session = async_sessionmaker(bind=_engine, class_=AsyncSession, expire_on_commit=False)
