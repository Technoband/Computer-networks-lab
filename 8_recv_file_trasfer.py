# receiver 
import socket

def receive_file(file_path, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        with open(file_path, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

if __name__ == '__main__':
    file_to_receive = 'received_file.txt'  # Set the path to the received file
    server_host = socket.gethostbyname(socket.gethostname())         # Set the server host
    server_port = 4455                    # Set the server port

    receive_file(file_to_receive, server_host, server_port)
