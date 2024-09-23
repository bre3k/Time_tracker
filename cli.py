from utils import create_user, delete_user, get_all_users, find_user_by_id
from utils import create_activity, delete_activity, get_all_activities, find_activity_by_id
from utils import create_session, delete_session, get_all_sessions, find_session_by_id

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Manage Users")
        print("2. Manage Activities")
        print("3. Manage Sessions")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            manage_users()
        elif choice == '2':
            manage_activities()
        elif choice == '3':
            manage_sessions()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

def manage_users():
    while True:
        print("\n--- Manage Users ---")
        print("1. Create User")
        print("2. Delete User")
        print("3. Display All Users")
        print("4. Find User by ID")
        print("5. Go Back")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter user name: ")
            create_user(name)
        elif choice == '2':
            user_id = input("Enter user ID to delete: ")
            delete_user(user_id)
        elif choice == '3':
            get_all_users()
        elif choice == '4':
            user_id = input("Enter user ID: ")
            find_user_by_id(user_id)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

def manage_activities():
    while True:
        print("\n--- Manage Activities ---")
        print("1. Create Activity")
        print("2. Delete Activity")
        print("3. Display All Activities")
        print("4. Find Activity by ID")
        print("5. Go Back")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter activity name: ")
            create_activity(name)
        elif choice == '2':
            activity_id = input("Enter activity ID to delete: ")
            delete_activity(activity_id)
        elif choice == '3':
            get_all_activities()
        elif choice == '4':
            activity_id = input("Enter activity ID: ")
            find_activity_by_id(activity_id)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

def manage_sessions():
    while True:
        print("\n--- Manage Sessions ---")
        print("1. Create Session")
        print("2. Delete Session")
        print("3. Display All Sessions")
        print("4. Find Session by ID")
        print("5. Go Back")
        choice = input("Choose an option: ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            activity_id = input("Enter activity ID: ")
            start_time = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
            end_time = input("Enter end time (optional, YYYY-MM-DD HH:MM:SS): ")
            create_session(user_id, activity_id, start_time, end_time)
        elif choice == '2':
            session_id = input("Enter session ID to delete: ")
            delete_session(session_id)
        elif choice == '3':
            get_all_sessions()
        elif choice == '4':
            session_id = input("Enter session ID: ")
            find_session_by_id(session_id)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()
