# 🔐 Python Authentication System (Hashed Password Version)

A simple authentication system built in Python with secure password hashing.

This version improves security by hashing all passwords using SHA-256 before storing them.

---

# ✨ Features

* User Registration
* User Login
* Change Password
* View Registered Users
* SHA-256 Password Hashing
* Duplicate Username Protection
* Password Length Validation

---

# 🔒 Security Upgrade

Passwords are no longer stored as plain text.

Example:

```python id="plain_password"
"Rahul123"
```

is stored as:

```python id="hashed_password"
"e2f044e3f084f..."
```

using SHA-256 hashing.

---

# 🚀 How To Run

Save the file as:

```bash id="run_filename"
auth_app.py
```

Run using:

```bash id="run_command"
python auth_app.py
```

---

# 📂 Functions

## register_user()

Registers a new user with a hashed password.

## login_user()

Checks username and hashed password.

## change_password()

Updates user password securely.

## view_users()

Displays registered usernames.

---

# 🛠 Technologies Used

* Python 3
* hashlib
* dictionaries
* functions
* loops
* conditionals



