import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


class Client:
    def __init__(self) -> None:
        self.sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
        self.server_address = "127.0.0.1"

    def connect_server(self):
        try:
            self.sock.connect(self.server_address)
        except socket.error as err:
            print(err)
            exit()

    def send_input(self, input):
        self.sock.sendall(input.encode("utf-8"))

    def receive_from_server(self):
        fake_content = ""
        self.sock.settimeout(1)
        fake_content += self.sock.recv(32).decode("utf-8")
        return fake_content


def close(self):
    self.sock.close()
