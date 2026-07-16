from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session

from .schemas import (
    CorsoCreate,
    CorsoUpdate,
    CorsoResponse
)

from .database import engine, get_db
from .models import Base, Corso as CorsoDB


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/corsi", response_model=list[CorsoResponse])
def ottenere_corsi(db: Session = Depends(get_db)):
    return db.query(CorsoDB).all()


@app.post("/corsi", response_model=CorsoResponse, status_code=status.HTTP_201_CREATED)
def creare_corso(corso: CorsoCreate, db: Session = Depends(get_db)):
    nuovo_corso = CorsoDB(
        nome=corso.nome,
        descrizione=corso.descrizione,
        livello=corso.livello,
        durata=corso.durata
    )

    db.add(nuovo_corso)
    db.commit()
    db.refresh(nuovo_corso)

    return nuovo_corso


@app.get("/corsi/{corso_id}", response_model=CorsoResponse)
def ottenere_corso(corso_id: str, db: Session = Depends(get_db)):
    corso = db.query(CorsoDB).filter(
        CorsoDB.id == corso_id
    ).first()

    if corso is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Corso non trovato"
        )

    return corso


@app.put("/corsi/{corso_id}", response_model=CorsoResponse)
def aggiornare_corso(corso_id: str, corso_update: CorsoUpdate, db: Session = Depends(get_db)):
    corso = db.query(CorsoDB).filter(
        CorsoDB.id == corso_id
    ).first()

    if corso is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Corso non trovato"
        )

    corso.nome = corso_update.nome
    corso.descrizione = corso_update.descrizione
    corso.livello = corso_update.livello
    corso.durata = corso_update.durata

    db.commit()
    db.refresh(corso)

    return corso


@app.delete("/corsi/{corso_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminare_corso(corso_id: str, db: Session = Depends(get_db)):
    corso = db.query(CorsoDB).filter(
        CorsoDB.id == corso_id
    ).first()

    if corso is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Corso non trovato"
        )

    db.delete(corso)
    db.commit()

    return None