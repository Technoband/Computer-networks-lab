# sender
import socket

def send_file(file_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")
        client_socket, client_address = server_socket.accept()

        with open(file_path, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.send(data)
        client_socket.close()

if __name__ == '__main__':
    file_to_send = 'hello.txt'  # Replace with the path to the file you want to send
    server_host = socket.gethostbyname(socket.gethostname())     # Set the server host (0.0.0.0 means all available network interfaces)
    server_port = 4455         # Set the server port
    send_file(file_to_send, server_host, server_port)
