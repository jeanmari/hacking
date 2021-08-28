#! /usr/bin/env python3

import sys
import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Simple Python\nPort Scanner")
print(ascii_banner)

ip = '127.0.0.1' # change ip add you want to scan
open_ports = []

ports = {21, 22, 23, 53, 80, 135, 443, 445} # change port # u want to scan

def probe_port(ip, port, result = 1):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((ip, port))
		if r == 0:
			result = r 
		sock.close()
	except Exception as e:
		pass
	return result

for port in ports:
	sys.stdout.flush()
	response = probe_port(ip, port)
	if response == 0:
		open_ports.append(port)

if open_ports:
	print("Open Ports are: ")
	print(sorted(open_ports))
else:
	print("Looks like no ports are open :(")
