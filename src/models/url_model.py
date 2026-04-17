from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, func
from datetime import datetime

from src.core.database import Base


class URL(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    url: Mapped[str] = mapped_column(String(2048), nullable=False)
    short_code: Mapped[str] = mapped_column(String(10), unique=True, index=True)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    access_count: Mapped[int] = mapped_column(default=0, server_default="0")