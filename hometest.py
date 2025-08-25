import socket
import threading
import time

# Function to handle each client
def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    client_socket.send(b"Welcome to the server!\n")

    while True:
        try:
            msg = client_socket.recv(1024)  # Receive data
            if not msg:
                break
            print(f"[{address}] {msg.decode().strip()}")
            client_socket.send(b"Message received!\n")
        except:
            break

    client_socket.close()
    print(f"[-] Connection closed for {address}")


# Main server function
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))   # Listen on port 5555
    server.listen(5)
    print("[*] Server started on port 5555")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()


if __name__ == "__main__":
    start_server()

