
# lock_tools.py
# Check account lock status and remaining login attempts.

def is_locked(failed, max_tries=3):
    """Return True if the account is locked."""
    return failed >= max_tries


def tries_left(failed, max_tries=3):
    """Return the number of remaining attempts."""
    if is_locked(failed, max_tries):
        return 0
    return max_tries - failed


def status(failed):
    """Return the account status."""
    if tries_left(failed) > 0:
        return f"active ({tries_left(failed)} tries left)"
    return "locked"


print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))
