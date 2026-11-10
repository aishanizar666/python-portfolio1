# fix_the_parser.py

LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
    # semantic error :makes it return the first 4 characters not 5
    return line[0:5]


def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
    #semantic error: user.lower() this wont change the oreginal string
    user = user.lower()
    return user


def is_failed(line):
    """Return True if the line reports a failed login."""
   # Semantic error: "failed" did not match "FAILED" because strings are case-sensitive.
    return line.find("FAILED")!=-1


def hide_first(user):
    """Return user with its first letter replaced by *."""
# Runtime error: strings are immutable, so user[0] = "*" raises TypeError.
    user = "*"+user[1:]
    return user


print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
# print(f"Length: {LINE.len()}") runtime error :this is error because len is not a method is a function
print(f"Length: {len(LINE)}")
