# login_decision.py - Checks login credentials and account lock status.

MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"

username = input("Username: ")
failed = int(input("Failed attempts so far: "))
password = input("Password: ")

if failed >= MAX_FAILED:
    print("Account locked.")
elif username != KNOWN_USER:
    print("Unknown user.")
elif password == STORED_PASSWORD:
    print("Access granted.")
else:
    attempts_left = MAX_FAILED - failed - 1
    print(f"Access denied. Attempts left: {attempts_left}")
