
# password_check.py
# Check password length and ensure it differs from the username.

def long_enough(password, minimum=8):
    """Return True if the password is long enough."""
    return len(password) >= minimum


def differs_from_username(password, username):
    """Return True if the password differs from the username."""
    return password != username


def password_ok(password, username):
    """Return True if both password checks pass."""
    return differs_from_username(password, username) and long_enough(password)


username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")
