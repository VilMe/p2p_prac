import socket
import sys


# def get_constants(prefix):
#     """ Create dictionary mapping socket module constants
#     to their names.
#     """
#     return {
#     getattr(socket, n): n 
#     for n in dir(socket) 
#     if n.startswith(prefix)
#     }

# families = get_constants('AF_')
# types = get_constants('SOCK_')
# protocols = get_constants('IPPROTO')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create an INET, STREAMing socket

# print('Family: ', families[sock.family])
# print('Type: ', types[sock.type])
# print('Protocol: ', protocols[sock.proto])
# print()
server_address = (sys.argv[1], 8080)
print('what port are we connecting to again..oh yeah, it\'s\n'
       '{}\non port {}'.format(*server_address))
sock.connect(server_address)



try:
    message = input('Enter message: ')
    print('sending {!r}'.format(message))
    message = message.encode('utf-8')
    print(message)
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
import socket
