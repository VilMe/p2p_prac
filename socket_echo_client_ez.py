import socket


def get_constants(prefix):
    """ Create dictionary mapping socket module constants
    to their names.
    """
    return {
    getattr(socket, n): n 
    for n in dir(socket) 
    if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO')

sock = socket.create_connection (('localhost', 8080))

print('Family: ', families[sock.family])
print('Type: ', types[sock.type])
print('Protocol: ', protocols[sock.proto])
print()

try:
    message = input('Enter message: ')
    print('sending {!r}'.format(message))
    message = message.encode('utf-8')
    sock.sendall(message)

    amount_received = 0
    amount_expected =len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket, buh bye!!')
    sock.close()
