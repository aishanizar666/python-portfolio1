# fix_the_rules

role = input("Role: ")

# convert the port input to int
port = int(input("Port: "))

# Semantic compare role using == not = 
is_admin = role == "admin"

# Syntax fix use <= instead of =<
is_system_port = port <= 1023

# Semantic fix: compare port on both sides of or.
is_web_port = port == 80 or port == 443

print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")