from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

from app.config import settings

Base = declarative_base()


def get_engine(database_url: str | None = None):
    url = database_url or settings.database_url
    engine_kwargs = {"future": True}

    if url.startswith("sqlite"):
        engine_kwargs["connect_args"] = {"check_same_thread": False}
        if ":memory:" in url:
            engine_kwargs["poolclass"] = StaticPool

    return create_engine(url, echo=settings.echo, **engine_kwargs)


def make_session_factory(database_url: str | None = None):
    engine = get_engine(database_url)
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
