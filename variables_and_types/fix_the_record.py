
name = "edge-router"

# syntax error -> ما بنفع يبدا اسم المتغير برقم
second_ip = "192.0.2.1"

# syntax error -> class is a reserved word
device_type = "router"

# run time error -> the string should be a number
port = int("22")

# run time error -> the varable should be declered
print("Device:", name)

print("Backup IP:", second_ip)
print("Type:", device_type)
print("Port:", port)
# all the errors are fixed :) 