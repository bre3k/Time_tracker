from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base



# Base ORM class
Base = declarative_base()

# Set up the database engine and session
engine = create_engine('sqlite:///time_tracker.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)

    sessions = relationship("Session", back_populates="user")

    # Property method to validate user name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("User name cannot be empty.")
        self._name = value


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)

    sessions = relationship("Session", back_populates="activity")

    # Property method to validate activity name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Activity name cannot be empty.")
        self._name = value


class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    activity_id = Column(Integer, ForeignKey('activities.id'))
    start_time = Column(DateTime, nullable=False)
    _end_time = Column("end_time", DateTime)

    user = relationship("User", back_populates="sessions")
    activity = relationship("Activity", back_populates="sessions")

    # Property method to ensure end_time is after start_time
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        if value and value <= self.start_time:
            raise ValueError("End time must be after start time.")
        self._end_time = value

# Function to set up the database schema
def setup_database():
    Base.metadata.create_all(engine)
    return session