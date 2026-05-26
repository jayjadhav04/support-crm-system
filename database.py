from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLite Database URL
DATABASE_URL = "sqlite:///./support_crm.db"


# Create Database Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Database Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base Class For Models
Base = declarative_base()