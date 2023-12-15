import os
import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


def client():
    # create socket
    # sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    server_address = './socket_file'

    print('Connecting to {}'.format(server_address))

    try:
        sock.connect(server_address)
        print('Successfully Connected!')

    # except sock.error as e:
    #     print(e)

    except FileNotFoundError:

        # stop program
        # A status code of 1 indicates a program error
        sys.exit(1)

    try:

        message = b'Sending a message to the server side'
        sock.sendall(message)
        sock.settimeout(2)
        print('waiting to receive')

    finally:
        print('closing socket')
        sock.close()


# send a message from user input


if __name__ == '__main__':
    client()
