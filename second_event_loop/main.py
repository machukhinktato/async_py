import socket
from select import select


to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen()


def accept_connection(server_socket):
    while True:
        client_socket, addr = server_socket.accept()
        print(f'connection from {addr}')


def send_message(client_socket):
    while True:
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = 'Hello world!\n'.encode()
            client_socket.send(response)

    print('Outside inner loop')
    client_socket.close()


def event_loop():
    while True:

        ready_to_read, _, _ = select(to_monitor, [], [])


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
