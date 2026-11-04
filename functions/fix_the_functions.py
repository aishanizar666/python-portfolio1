
# fix_the_functions.py
# Fix runtime and semantic errors in a login report.

def print_header():
    """Display the report header."""
    print("=" * 30)
    print("LOGIN REPORT")
    print("=" * 30)


# Runtime error (NameError):
# The function must be defined before it is called.
print_header()


def lock_minutes(failed, minutes=15):
    """Return failed * minutes if failed >= 3, else 0."""
    if failed >= 3:
        # Semantic error:
        # The original code calculated the result but returned 0.
        return failed * minutes
    return 0


def login_line(username, failed):
    """Return one line of the report."""
    minutes = lock_minutes(failed)
    return f"{username}: {failed} failed, locked {minutes} min"


# Runtime error (TypeError):
# The parameter is named username, not user.
print(login_line(username="sara", failed=4))

# Semantic error:
# The function returns a string, but it must be printed.
print(login_line("omar", 1))
