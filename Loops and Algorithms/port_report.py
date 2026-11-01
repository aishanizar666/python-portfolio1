
# port_report.py
# Classifies ports in a given range and counts the checked ports.

start = int(input("Start port: "))
end = int(input("End port: "))

count = 0

for port in range(start, end + 1):
    if port <= 1023:
        print(f"{port}: system")
    elif port <= 49151:
        print(f"{port}: user")
    else:
        print(f"{port}: dynamic")

    count += 1

print(f"Ports checked: {count}")
