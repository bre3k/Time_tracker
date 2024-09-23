from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the Base class
Base = declarative_base()

# Create the database engine (you can customize the path to your database)
engine = create_engine('sqlite:///time_tracker.db', echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)

# Create a session instance
session = SessionLocal()
