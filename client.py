import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '127.0.0.1'
client_address = '127.0.0.2'


def client():
    print('Connecting to {}'.format(server_address))

    try:
        sock.connect(server_address)
        print('Successfully Connected!')

    except sock.error as e:
        print(e)

    except FileNotFoundError:

        # stop program
        # A status code of 1 indicates a program error
        sys.exit(1)

    message = b'Sending a message to the server side'

    try:
        sock.sendto(message, server_address)
        sock.settimeout(2)

        try:
            while True:
                resource = sock.recv(64)
                if resource:
                    print('Server response: {}'.format(resource))
                else:
                    break
        except TimeoutError as e:
            print(e)
    finally:
        print('closing socket')
        sock.close()


if __name__ == '__main__':
    client()
