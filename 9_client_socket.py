#client
import socket
import time

def main():
    host = "192.168.137.1"
    port = 4545
    message = "Welcome to network programming world"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    c = 0
    while c < 4:
        t1 = int(round(time.time() * 1000))
        client_socket.send(message.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        t2 = int(round(time.time() * 1000))
        print(response)
        print(f"TTL = {t2 - t1} ms")
        c += 1
    client_socket.close()

if __name__ == '__main__':
    main()