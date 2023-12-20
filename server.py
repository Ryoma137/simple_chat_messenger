import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '127.0.0.1'


def server():
    # check if file exists
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('Starting up on {}'.format(server_address))

    # bind a socket to server address
    sock.bind(server_address)

    # wait for a connection request
    sock.listen(1)

    while True:
        # accept connection from client-side
        connection, client_address = sock.accept()
        try:
            print('Connection from'.format(client_address))

            data = connection.recv(1024)
            decoded_data = data.decode('utf-8')

            print('Received', decoded_data)

        except ConnectionError as e:
            print(e)

        finally:
            print("Closing current connection")
            connection.close()


if __name__ == '__main__':
    server()
