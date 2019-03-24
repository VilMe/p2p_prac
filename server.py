import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create an INET, STREAMing socket
server_address = ('localhost', 8080)
#store socket address in a variable
print('starting up on {}, port {}'.format(*server_address))
serv.bind(server_address)

serv.listen(5)

while True:
	print('connection? anyone?\nGoing, once...\nGoing twice...\nWaiting for a connection, yo')
	connection, client_address = serv.accept()

	try:
		print('connection from: ', client_address)
		while True:
			data = connection.recv(16)
			print('print {!r}',format(data))
			if data: 
				print('sending data back to client')
				connection.sendall(data)
			else:
				print('no data from ', client_address)
				break
	finally:
		connection.close()
