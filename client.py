import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create an INET, STREAMing socket

server_address = ('localhost', 8080)
print('connect to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = input('Enter message: ')
    print('sending {!r}'.format(message))
    message = message.encode('utf-8')
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket, buh bye!')
    sock.close()
