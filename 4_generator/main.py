import selectors
from socket import *


# David Beazley, 2015 pyconn, concurrency from the ground up live

def server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5001))
    server_socket.listen()

    while True:
        yield 'read', server_socket
        client_socket, addr = server_socket.accept()
        print('Connection from ', addr)
        client(client_socket)


def client(client_socket):
    while True:
        yield 'read', client_socket
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = 'Hello world!\n'.encode()
            yield 'send', client_socket
            client_socket.send(response)
    client_socket.close()


def event_loop():
    while True:
        pass


if __name__ == '__main__':
    server()
