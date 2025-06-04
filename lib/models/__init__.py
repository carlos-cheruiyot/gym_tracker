# models/__init__.py
from database.db import Base, engine
from models.member import Member
from models.workout_session import WorkoutSession

def create_tables():
    Base.metadata.create_all(engine)
