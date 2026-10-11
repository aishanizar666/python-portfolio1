

# Predictions:
# int(" 22 ") -> Works: surrounding spaces are ok
# int("+22")  -> Works: a leading plus sign 
# int("0022") -> Works: leading zeros are accepted 
# int("2_2") -> Works: one underscore between digits is accepted in python

print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))

# Documentation:
# https://docs.python.org/3/library/functions.html#int