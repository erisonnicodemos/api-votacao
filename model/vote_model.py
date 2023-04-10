from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./bbbdatabase.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    paredao_id = Column(Integer, ForeignKey("paredao.id"))

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class VoteModel:
    def create(self, db, candidate_id: int, paredao_id: int):
        vote = Vote(candidate_id=candidate_id, paredao_id=paredao_id)
        db.add(vote)
        db.commit()
        db.refresh(vote)
        return vote
