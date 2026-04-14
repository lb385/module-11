import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from app.db import Base


@pytest.fixture()
def engine():
    database_url = os.getenv("TEST_DATABASE_URL", os.getenv("DATABASE_URL", "sqlite+pysqlite:///:memory:"))
    engine_kwargs = {"future": True}

    if database_url.startswith("sqlite"):
        engine_kwargs["connect_args"] = {"check_same_thread": False}
        if ":memory:" in database_url:
            engine_kwargs["poolclass"] = StaticPool

    engine = create_engine(database_url, **engine_kwargs)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture()
def session(engine):
    Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
    with Session() as session:
        yield session
