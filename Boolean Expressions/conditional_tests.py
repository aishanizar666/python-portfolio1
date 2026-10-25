# conditional_test
A = "first"
B = "second"
num = 3
n = 22

print("Is num >= 3? I predict True.")
print(num >= 3)

print("\nIs n == 22? I predict True.")
print(n == 22)

print("\nIs B != 'admin'? I predict True.")
print(B != "admin")

print("\nIs num > 2? I predict True.")
print(num > 2)

print("\nIs num <= 3 and n < 100? I predict True.")
print(num <= 3 and n < 100)

print("\nIs B == 'admin'? I predict False.")
print(B == "admin")

print("\nIs n > 1023? I predict False.")
print(n > 1023)

print("\nIs num < 3? I predict False.")
print(num < 3)

print("\nIs B == 'root' or n == 80? I predict False.")
print(B == "root" or n == 80)

print("\nIs not (A == 'first')? I predict False.")
print(not (A == "first"))