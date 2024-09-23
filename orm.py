from models import User, Session, Activity, session  

def create_user(name):
    try:
        user = User(name=name)
        session.add(user)
        session.commit()
        print(f"User '{name}' created successfully.")
        return user
    except ValueError as e:
        print(f"Error: {e}")

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
