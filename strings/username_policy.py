
# username_policy.py
# Validate a username according to the username policy.

MIN_LENGTH = 3
MAX_LENGTH = 12


def clean(username):
    """Return the username stripped and in lowercase."""
    return username.strip().lower()


def bad_character(username):
    """Return the first invalid character, or an empty string."""
    for char in username:
        if not char.isalnum() and char != '_':
            return char
    return ""


def policy_problem(username):
    """Return the first username policy problem, or an empty string."""
    if not (MIN_LENGTH <= len(username) <= MAX_LENGTH):
        return "length must be 3 to 12"

    if not username[0].isalpha():
        return "it must start with a letter"

    bad = bad_character(username)
    if bad != "":
        return f"the character {bad} is not allowed"

    return ""


username = clean(input("New username: "))
problem = policy_problem(username)

if problem == "":
    print(f"Accepted [{username}].")
else:
    print(f"Rejected [{username}]: {problem}.")
