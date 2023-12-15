import os
import socket
import sys


def server():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = './socket_file'

    # check if file exists
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('Starting up on {}'.format(server_address))

    # bind a socket to server address
    sock.bind(server_address)

    # wait connection request
    sock.listen(1)

    while True:

        # accept connection from client-side
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            while True:
                data = connection.recv(32)

                decoded_data = data.decode('utf-8')
                print('Received ' + decoded_data)

                if data:

                    response = 'Processing ' + decoded_data

                    # return message to client
                    connection.sendall(response.encode())

                # done a loop if data is not sent from client-side
                else:
                    print('no data from', client_address)
                    break
        finally:
            print("Closing current connection")
            connection.close()


if __name__ == '__main__':
    server()
