
# port_classifier.py - Validates and classifies network ports by range and service.

port = int(input("Port: "))

if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
else:
    if port <= 1023:
        print("Range: system")
    elif port <= 49151:
        print("Range: user")
    else:
        print("Range: dynamic or private")

    if port == 22:
        print("Service: ssh")
    elif port == 80:
        print("Service: http")
    elif port == 443:
        print("Service: https")
