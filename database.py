from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABASE = "sqlite+aiosqlite:///db.sqlite3"
engine = create_engine(URL_DATABASE, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()
