
# conditional_tests.py - Predicts and tests ten Boolean expressions.

user = "analyst"
role = "viewer"
failed = 3
port = 22

print("Is failed >= 3? I predict True.")
print(failed >= 3)

print("\nIs port == 22? I predict True.")
print(port == 22)

print("\nIs role != 'admin'? I predict True.")
print(role != "admin")

print("\nIs failed > 2? I predict True.")
print(failed > 2)

print("\nIs failed <= 3 and port < 100? I predict True.")
print(failed <= 3 and port < 100)

print("\nIs role == 'admin'? I predict False.")
print(role == "admin")

print("\nIs port > 1023? I predict False.")
print(port > 1023)

print("\nIs failed < 3? I predict False.")
print(failed < 3)

print("\nIs role == 'root' or port == 80? I predict False.")
print(role == "root" or port == 80)

print("\nIs not (user == 'analyst')? I predict False.")
print(not (user == "analyst"))
