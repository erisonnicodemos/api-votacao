from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./bbbdatabase.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CandidateModel:
    def create(self, db, name: str):
        candidate = Candidate(name=name)
        db.add(candidate)
        db.commit()
        db.refresh(candidate)
        return candidate

    def read(self, db, candidate_id: int):
        candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
        return candidate
