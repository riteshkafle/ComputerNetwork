import socket
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    print("Connected to server.")
    message = "Hello Server! This is the client."
    client_socket.send(message.encode())
    print(f"Sent to server: {message}")
    response = client_socket.recv(1024).decode()
    print(f" Received from server: {response}")
    client_socket.close()
if __name__ == "__main__":
    start_client()
