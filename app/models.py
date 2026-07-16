import uuid

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Corso(Base):
    __tablename__ = "corsi"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    descrizione: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    livello: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    durata: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )