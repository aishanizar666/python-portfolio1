# security_toolkit.py
# Provide a menu of simple security utilities.

MIN_LENGTH = 8

def border(width):
    """Print a horizontal box border."""
    print('+' + '-' * (width + 2) + '+')


def show_box(text):
    """Display text inside a box."""
    border(len(text))
    print('| ' + text + ' |')
    border(len(text))


def port_range(port):
    """Return the category of a port number."""
    if port < 0 or port > 65535:
        return "invalid"
    elif 0 <= port <= 1023:
        return "system"
    elif 1024 <= port <= 49151:
        return "user"
    else:
        return "dynamic"


def check_port():
    """Ask for a port and display its category."""
    port = int(input("Port: "))
    show_box("Port " + str(port) + ": " + port_range(port))


def password_problem(password,username):
    """Return the first password problem, or an empty string."""
    if len(password)<MIN_LENGTH :
        return "too short"
    elif password == username:
        return "same as the username"
    else :
        return ""


def check_password():
    """Ask for credentials and display the password result."""
    username = input("Username: ")
    password = input("Password: ")

    result = password_problem(password, username)

    if result == "":
        answer = "Password accepted"
    else:
        answer = "Rejected: " + result

    show_box(answer)


def days_to_guess(digits, per_second):
    """Return the number of full days needed to guess a PIN."""
    return 10 ** digits // (per_second * 86400)



def check_pin():
    """Ask for PIN details and display the guessing time."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))

    days = days_to_guess(digits, per_second)
    result = str(digits) + " digits: " + str(days) + " days"

    show_box(result)


def show_menu():
    """Display the security toolkit menu."""
    print("SECURITY TOOLKIT\n1. Check a port\n2. Check a password\n3. PIN guessing time\nq. Quit")


show_menu()
checks = 0
while True:
    choice = input("Choice (1,2,3,or q) : ")
    if choice == '1':
        check_port()
        checks+=1
    elif choice == '2':
        check_password()
        checks+=1
    elif choice== '3' :
        check_pin()
        checks+=1
    elif choice == 'q':
        show_box(f"Checks done: {checks}")
        break
    else : 
        print("Unknown choice.")
    