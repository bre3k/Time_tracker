from base import engine, Base
from models import User, Activity, Session

# Create all tables in the database
Base.metadata.create_all(engine)
print("Database and tables created successfully.")

