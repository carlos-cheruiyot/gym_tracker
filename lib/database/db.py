# database/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///gym_tracker.db", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()
