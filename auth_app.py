import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


users = {
    "Advik": hash_password("Advik876*)("),
    "Shourya": hash_password("YuIOrt56%^&!@#"),
    "Alex": hash_password("*HgjiKL"),
    "God": hash_password("()&908!@#")
}


def register_user(users, username, password):

    if username in users:
        return "Username already exists!"

    if len(password) < 6:
        return "Password too short"

    users[username] = hash_password(password)

    return "User registered successfully"


def login_user(users, username, password):

    username = username.strip()

    if username not in users:
        return "Username not found!"

    if users[username] != hash_password(password):
        return "Incorrect password"

    return "Login successful"


def change_password(users, username, old_password, new_password):

    if username not in users:
        return "Username not found!"

    if users[username] != hash_password(old_password):
        return "Old password incorrect"

    if len(new_password) < 6:
        return "New password too short"

    users[username] = hash_password(new_password)

    return "Password updated successfully!"


def view_users(users):

    if not users:
        return "No users found"

    print("\nRegistered Users:")
    for username in users:
        print(username)


# TESTING

print(register_user(users, "Rahul", "Rahul123"))
print(login_user(users, "Rahul", "Rahul123"))
print(change_password(users, "Rahul", "Rahul123", "NewPass456"))

view_users(users)

# View hashed passwords
print("\nStored Data:")
print(users)
