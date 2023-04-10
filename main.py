from click import DateTime
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from controller.candidate_controller import CandidateController
from controller.paredao_controller import ParedaoController
from controller.vote_controller import VoteController
from model import get_db

app = FastAPI()

@app.post("/candidates")
def create_candidate(name: str, controller: CandidateController = Depends()):
    return controller.create_candidate(name)

@app.get("/candidates/{candidate_id}")
def read_candidate(candidate_id: int, controller: CandidateController = Depends()):
    return controller.read_candidate(candidate_id)

@app.post("/paredao")
def create_paredao(edicao: str, numero_paredao: int, data_inicio: DateTime, data_fim: DateTime, controller: ParedaoController = Depends()):
    return controller.create_paredao(edicao, numero_paredao, data_inicio, data_fim)

@app.post("/vote")
def vote_for_candidate(candidate_id: int, paredao_id: int, controller: VoteController = Depends()):
    return controller.vote_for_candidate(candidate_id, paredao_id)

@app.get("/paredao/{paredao_id}/votes")
def list_candidates_with_votes(paredao_id: int, controller: ParedaoController = Depends()):
    return controller.list_candidates_with_votes(paredao_id)
