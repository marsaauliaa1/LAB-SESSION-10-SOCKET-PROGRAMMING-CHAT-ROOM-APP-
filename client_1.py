import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('192.168.56.1', 12345))

client_socket.send("Halo client_2!".encode())

response = client_socket.recv(1024).decode()
print(f"Balasan dari server: {response}")

client_socket.close()
