from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from model import VoteModel, get_db, CandidateModel, ParedaoModel

class VoteController:
    def __init__(self):
        self.model = VoteModel()
        self.candidate_model = CandidateModel()
        self.paredao_model = ParedaoModel()

    def vote_for_candidate(self, candidate_id: int, paredao_id: int, db: Session = Depends(get_db)):
        candidate = self.candidate_model.read(db, candidate_id)
        if not candidate:
            return None
        paredao = self.paredao_model.read(db, paredao_id)
        if not paredao:
            return None
        self.model.create(db, candidate_id, paredao_id)
        return candidate
