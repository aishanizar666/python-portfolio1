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
        return "Too short"
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

def days_to_guess(digits,per_second):
    """this function is calculating the number of dayes to guss a pin number of variable number of digites"""
    return 10**digits // (per_second*86400)

def chead_pin():
    dig = int(input("PIN digites: "))
    GPS = int(input("Guesses per second : "))
    result = str(dig)+" digites: "+str(days_to_guess(dig,GPS)) +" days"
    show_box(result)
chead_pin()