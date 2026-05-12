import hashlib

FILE_NAME = "users.txt"


# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Load users from file
def load_users():
    users = {}

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:
                username, password = line.strip().split(",")

                users[username] = password

    except FileNotFoundError:
        pass

    return users


# Save users to file
def save_users(users):

    with open(FILE_NAME, "w") as file:

        for username, password in users.items():
            file.write(f"{username},{password}\n")


# Register
def register_user(users):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users:
        print("Username already exists!")
        return

    if len(password) < 6:
        print("Password too short")
        return

    users[username] = hash_password(password)

    save_users(users)

    print("User registered successfully")


# Login
def login_user(users):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("Username not found!")
        return

    if users[username] != hash_password(password):
        print("Incorrect password")
        return

    print("Login successful")


# Change password
def change_password(users):

    username = input("Enter username: ")
    old_password = input("Enter old password: ")
    new_password = input("Enter new password: ")

    if username not in users:
        print("Username not found!")
        return

    if users[username] != hash_password(old_password):
        print("Old password incorrect")
        return

    if len(new_password) < 6:
        print("New password too short")
        return

    users[username] = hash_password(new_password)

    save_users(users)

    print("Password updated successfully!")


# Delete account
def delete_user(users):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username not in users:
        print("Username not found!")
        return

    if users[username] != hash_password(password):
        print("Incorrect password")
        return

    del users[username]

    save_users(users)

    print("Account deleted successfully")


# View users
def view_users(users):

    if not users:
        print("No users found")
        return

    print("\nRegistered Users:")

    for username in users:
        print(username)


# MAIN PROGRAM
users = load_users()

while True:

    print("\n=== AUTH SYSTEM ===")
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
