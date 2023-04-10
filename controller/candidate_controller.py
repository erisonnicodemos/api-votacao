from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from model import CandidateModel, get_db

class CandidateController:
    def __init__(self):
        self.model = CandidateModel()

    def create_candidate(self, name: str, db: Session = Depends(get_db)):
        return self.model.create(db, name)

    def read_candidate(self, candidate_id: int, db: Session = Depends(get_db)):
        candidate = self.model.read(db, candidate_id)
        if not candidate:
            raise HTTPException(status_code=404, detail="Candidate not found")
        return candidate
