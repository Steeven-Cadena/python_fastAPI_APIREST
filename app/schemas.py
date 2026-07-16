from pydantic import BaseModel, ConfigDict


class CorsoCreate(BaseModel):
    nome: str
    descrizione: str | None = None
    livello: str
    durata: int

    model_config = ConfigDict(extra="forbid")


class CorsoUpdate(BaseModel):
    nome: str
    descrizione: str | None = None
    livello: str
    durata: int

    model_config = ConfigDict(extra="forbid")


class CorsoResponse(BaseModel):
    id: str
    nome: str
    descrizione: str | None = None
    livello: str
    durata: int

    model_config = ConfigDict(from_attributes=True)