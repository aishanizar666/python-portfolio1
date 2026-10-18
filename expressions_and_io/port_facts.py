# RFC 9293: https://www.rfc-editor.org/rfc/rfc9293
# RFC 791: https://www.rfc-editor.org/rfc/rfc791

PORT_BITS = 16
IPV4_BITS = 32

total_ports = 2 ** PORT_BITS
highest_port = 2 ** PORT_BITS - 1
total_ipv4_addresses = 2 ** IPV4_BITS

print(f"Possible port numbers: {total_ports}")
print(f"Highest port number: {highest_port}")
print(f"Possible IPv4 addresses: {total_ipv4_addresses}")