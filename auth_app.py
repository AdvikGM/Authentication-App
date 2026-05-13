import hashlib
import json
import os

FILE_NAME = "users.json"



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def load_users():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r") as file:
        return json.load(file)



def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)



def register_user(users):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("Username already exists!")
        return

    if len(password) < 6:
        print("Password too short")
        return

    users[username] = {
        "password": hash_password(password),
        "locked": False,
        "attempts": 0
    }

    save_users(users)
    print("User registered successfully!")



def login_user(users):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("Username not found!")
        return None

    if users[username]["locked"]:
        print("Account is locked!")
        return None

    if users[username]["password"] == hash_password(password):
        print("Login successful!")
        users[username]["attempts"] = 0
        save_users(users)
        return username

    else:
        print("Incorrect password!")
        users[username]["attempts"] += 1

        if users[username]["attempts"] >= 3:
            users[username]["locked"] = True
            print("Account locked due to too many attempts!")

        save_users(users)
        return None



def change_password(users):

    username = input("Enter username: ")
    old_password = input("Enter old password: ")
    new_password = input("Enter new password: ")

    if username not in users:
        print("Username not found!")
        return

    if users[username]["password"] != hash_password(old_password):
        print("Old password incorrect")
        return

    if len(new_password) < 6:
        print("New password too short")
        return

    users[username]["password"] = hash_password(new_password)
    save_users(users)

    print("Password updated successfully!")



def delete_user(users):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("Username not found!")
        return

    if users[username]["password"] != hash_password(password):
        print("Incorrect password")
        return

    del users[username]
    save_users(users)

    print("Account deleted successfully!")



def view_users(users):

    if not users:
        print("No users found")
        return

    print("\nRegistered Users:")
    for username in users:
        status = "LOCKED" if users[username]["locked"] else "ACTIVE"
        print(f"{username} - {status}")



users = load_users()

while True:

    print("\n=== AUTH SYSTEM  ===")
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Delete Account")
    print("5. View Users")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        register_user(users)

    elif choice == "2":
        login_user(users)

    elif choice == "3":
        change_password(users)

    elif choice == "4":
        delete_user(users)

    elif choice == "5":
        view_users(users)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
