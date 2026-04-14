from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    database_url: str = os.getenv("DATABASE_URL", "sqlite+pysqlite:///:memory:")
    echo: bool = os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true"


settings = Settings()
