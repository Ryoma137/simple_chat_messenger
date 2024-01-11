from client import Client
from server import Server


def print_description():
    print(
        """
        Fake content will be sent when user input following type.
        name -> fake name, address -> fake address, email -> fake email, text -> fake text, exit -> Exit Program
        """
    )


def main():
    client = Client()
    server = Server()

    client.connect_server()
    server.accept_client()

    print_description()

    while True:
        user_input = input('---Which one do you pick up---?')

        if user_input == "exit":
            break

        client.send_input(user_input)
        server.receive_and_send_fake()

        fake_content = client.receive_from_server()
        print(fake_content)

    client.close()
    server.close()


if __name__ == "__main__":
    main()
