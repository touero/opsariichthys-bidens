from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///database/all_school.db'
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
