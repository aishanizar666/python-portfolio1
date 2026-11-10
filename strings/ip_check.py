
# ip_check.py
# Validate an IPv4 address.

def is_valid_part(part):
    """Return True if the part contains only digits and is at most 255."""
    return part.isdigit() and 0 <= int(part) <= 255


def ip_problem(address):
    """Return the first IPv4 problem, or an empty string."""
    if address.count('.') != 3:
        return "Invalid: it needs exactly 3 dots."

    parts = address.split('.')

    if "" in parts:
        return "Invalid: a part is empty."

    for part in parts:
        if not is_valid_part(part):
            return f"Invalid: {part} is not a number from 0 to 255."

    return ""


address = input("IPv4 address: ").strip()
problem = ip_problem(address)

if problem == "":
    print(f"{address} is valid.")
else:
    print(problem)
