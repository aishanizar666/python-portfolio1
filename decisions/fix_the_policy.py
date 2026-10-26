
# fix_the_policy.py

MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

# Syntax error: the colon (:)was missing after the if condition
if len(password) < MIN_LENGTH:
    print("- Too short.")

# Semantic error: use a separate if so both warnings can appear
if password == username:
    print("- Same as the username.")

# Semantic error: check >= 16 first, otherwise long passwords are classified as acceptable.
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

# Semantic error: move the print outside the else block so it always executes.
print(f"Length: {len(password)} ({strength})")
