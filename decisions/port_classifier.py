#port_classifier

port = int(input("enter the port number : "))

if 0<=port<=65535:
    if port<=1023:
        print("Range : system ")
    elif port<=49151:
        print("Range : user")
    else :
        print("Range : dynamic or private ")
    if port == 22:
        print("Service : ssh")
    elif port == 80:
        print("Service : http")
    elif port == 443:
        print("Service : https")
else :
    print("Invalid port !")