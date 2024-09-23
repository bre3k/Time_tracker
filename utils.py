from models import User, Activity, Session, session
from datetime import datetime


# User CRUD
def create_user(name):
    if not name:
        print("Error: Name cannot be empty.")
        return
    try:
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"User '{name}' created successfully.")
        return user
    except Exception as e:
        print(f"Error creating user: {e}")

def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User '{user.name}' deleted.")
    else:
        print(f"No user found with ID {user_id}.")

def get_all_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}")

def find_user_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        print(f"ID: {user.id}, Name: {user.name}")
        return user
    else:
        print(f"No user found with ID {user_id}.")

# Activity CRUD
def create_activity(name):
    if not name:
        print("Error: Name cannot be empty.")
        return
    try:
        activity = Activity(name=name)
        session.add(activity)
        session.commit()
        print(f"Activity '{name}' created successfully.")
        return activity
    except Exception as e:
        print(f"Error creating activity: {e}")

def delete_activity(activity_id):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        session.delete(activity)
        session.commit()
        print(f"Activity '{activity.name}' deleted.")
    else:
        print(f"No activity found with ID {activity_id}.")

def get_all_activities():
    activities = session.query(Activity).all()
    for activity in activities:
        print(f"ID: {activity.id}, Name: {activity.name}")

def find_activity_by_id(activity_id):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if activity:
        print(f"ID: {activity.id}, Name: {activity.name}")
        return activity
    else:
        print(f"No activity found with ID {activity_id}.")

# Session CRUD
def create_session(user_id, activity_id, start_time, end_time=None):
    try:
        session_obj = Session(user_id=user_id, activity_id=activity_id, start_time=start_time, end_time=end_time)
        session.add(session_obj)
        session.commit()
        print("Session created successfully.")
        return session_obj
    except Exception as e:
        print(f"Error creating session: {e}")

def delete_session(session_id):
    session_obj = session.query(Session).filter_by(id=session_id).first()
    if session_obj:
        session.delete(session_obj)
        session.commit()
        print("Session deleted.")
    else:
        print(f"No session found with ID {session_id}.")

def get_all_sessions():
    sessions = session.query(Session).all()
    for s in sessions:
        print(f"ID: {s.id}, User ID: {s.user_id}, Activity ID: {s.activity_id}, Start: {s.start_time}, End: {s.end_time}")

def find_session_by_id(session_id):
    session_obj = session.query(Session).filter_by(id=session_id).first()
    if session_obj:
        print(f"ID: {session_obj.id}, User ID: {session_obj.user_id}, Activity ID: {session_obj.activity_id}")
        return session_obj
    else:
        print(f"No session found with ID {session_id}.")

def calculate_session_duration(start_time: datetime, end_time: datetime) -> int:
    """Calculate the duration of a session in seconds."""
    return int((end_time - start_time).total_seconds())

def format_duration(seconds: int) -> str:
    """Format a duration in seconds to a human-readable string."""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"
