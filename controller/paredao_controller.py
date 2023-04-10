from click import DateTime
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from model import ParedaoModel, get_db

class ParedaoController:
    def __init__(self):
        self.model = ParedaoModel()

    def create_paredao(self, edicao: str, numero_paredao: int, data_inicio: DateTime, data_fim: DateTime, db: Session = Depends(get_db)):
        return self.model.create(db, edicao, numero_paredao, data_inicio, data_fim)
