import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")
    conn, addr = server_socket.accept()
    print(f"Connected to client at {addr}")
    message = conn.recv(1024).decode()
    print(f"Received from client: {message}")
    response = "Hello Client! Your message was received."
    conn.send(response.encode())
    conn.close()

if __name__ == "__main__":
    start_server()
