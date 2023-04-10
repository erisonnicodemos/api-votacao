from ast import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "sqlite:///./bbbdatabase.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

candidates_paredao = Table('candidates_paredao', Base.metadata,
    Column('candidate_id', Integer, ForeignKey('candidates.id')),
    Column('paredao_id', Integer, ForeignKey('paredao.id'))
)

class Paredao(Base):
    __tablename__ = "paredao"

    id = Column(Integer, primary_key=True, index=True)
    edicao = Column(String)
    numero_paredao = Column(Integer)
    data_inicio = Column(DateTime)
    data_fim = Column(DateTime)

    candidates = relationship("Candidate", secondary=candidates_paredao, back_populates="paredaos")

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    paredaos = relationship("Paredao", secondary=candidates_paredao, back_populates="candidates")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ParedaoModel:
    def create(self, db, edicao: str, numero_paredao: int, data_inicio: DateTime, data_fim: DateTime, candidate_ids: List[int] = []):
        paredao = Paredao(edicao=edicao, numero_paredao=numero_paredao, data_inicio=data_inicio, data_fim=data_fim)
        for candidate_id in candidate_ids:
            candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
            paredao.candidates.append(candidate)
        db.add(paredao)
        db.commit()
        db.refresh(paredao)
        return paredao

    def read(self, db, paredao_id: int):
        paredao = db.query(Paredao).filter(Paredao.id == paredao_id).first()
        return paredao

class ParedaoModel:
    def create(self, db, edicao: str, numero_paredao: int, data_inicio: DateTime, data_fim: DateTime, candidate_ids: List[int] = []):
        paredao = Paredao(edicao=edicao, numero_paredao=numero_paredao, data_inicio=data_inicio, data_fim=data_fim)
        for candidate_id in candidate_ids:
            candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
            paredao.candidates.append(candidate)
        db.add(paredao)
        db.commit()
        db.refresh(paredao)
        return paredao

    def read(self, db, paredao_id: int):
        paredao = db.query(Paredao).filter(Paredao.id == paredao_id).first()
        return paredao

    def list_candidates_with_votes(self, db, paredao_id: int):
        paredao = self.read(db, paredao_id)
        candidates = []
        for candidate in paredao.candidates:
            candidates.append({"id": candidate.id, "name": candidate.name, "votes": candidate.votes})
        return candidates
