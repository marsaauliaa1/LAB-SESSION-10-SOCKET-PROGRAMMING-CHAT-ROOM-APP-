import socket
import threading

def handle_client(client_socket, client_address):
    print(f"[+] Terhubung dengan {client_address}")
    try:
        data = client_socket.recv(1024).decode()
        print(f"[{client_address}] Pesan: {data}")
        client_socket.send("Halo kenalan yuk!".encode())
    except Exception as e:
        print(f"[!] Error dengan {client_address}: {e}")
    finally:
        client_socket.close()
        print(f"[-] Koneksi dengan {client_address} ditutup.")

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('172.16.49.109', 12345))
server_socket.listen(5)

print("[*] Server aktif, menunggu koneksi di port 12345... ")

while True:
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address))

    client_thread.start()
