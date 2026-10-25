# truth_research
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# False: An empty string is falsy.
print(bool(""))

# True: "0" is a non-empty string.
print(bool("0"))

# False: The integer zero is falsy.
print(bool(0))

# False: The floating point zero is falsy.
print(bool(0.0))

# True: "False" is a non empty string.
print(bool("False"))

# in conclusion any non empty string is true and zeros,empty strings and empty data types are false