# models/workout_session.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class WorkoutSession(Base):
    __tablename__ = 'workout_sessions'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    date = Column(Date, nullable=False)
    duration_min = Column(Integer, nullable=False)
    workout_type = Column(String, nullable=False)
    notes = Column(String)

    member = relationship("Member", back_populates="workout_sessions")

    def __repr__(self):
        return f"<WorkoutSession(id={self.id}, member_id={self.member_id}, type={self.workout_type})>"
