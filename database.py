from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# #SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/dbname"
SQLALCHEMY_DATABASE_URL = "postgresql://ammar.panaverse.dao:gf2PhRClEsT6@ep-calm-meadow-04776546.ap-southeast-1.aws.neon.tech/TodoDB?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

Base.metadata.create_all(bind=engine)
