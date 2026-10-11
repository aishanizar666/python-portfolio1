# هذا الكود بعرض معلومات عن شبكة 

MAX_CONNECTIONS = 50

device_name = "Aisha-laptop"
device_ip = "192.0.2.15"
service = "HTTP"
open_port = 80

print("Device:", device_name)
print("IP address:", device_ip)
print("Service:", service)
print("Port:", open_port)
print("Max connections:", MAX_CONNECTIONS)


# تحديث للقيم اللي موجودة
service = "HTTPS"
open_port = 90

print("Updated service:", service, "on port", open_port)