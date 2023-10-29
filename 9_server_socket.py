#server
import socket
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.137.1', 4545))
    server_socket.listen(1)

    print("Ping server is running on port 4545...")

    while True:
        client_socket, _ = server_socket.accept()

        c = 0
        while c < 4:
            message = client_socket.recv(1024).decode('utf-8')
            response = f"Reply from {socket.gethostname()}; Length {len(message)}"
            client_socket.send(response.encode('utf-8'))
            c += 1

        client_socket.close()

if __name__ == '__main__':
    main()


