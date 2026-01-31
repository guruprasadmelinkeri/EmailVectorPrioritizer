from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os 
from dotenv import load_dotenv


DATABASE_URL = "sqlite:///./emails.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)
engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

