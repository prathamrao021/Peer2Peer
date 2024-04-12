import socket
import sys
import threading
import os

# def handle_client(client_socket, client_address):
#     reading_thread = threading.Thread(target=read_data, args=(client_socket, client_address))
#     # writing_thread = threading.Thread(target=write_data, args=(client_socket, client_address))

#     reading_thread.start()
#     # writing_thread.start()

#     reading_thread.join()
#     # writing_thread.join()
# def read_data(client_socket, client_address):
#     while True:
#         data = client_socket.recv(1024)
#         if not data:
#             break
#         print("Received from "+str(client_address)+": ", data.decode())
#         if data.decode() == "exit":
#             break

# def write_data(client_socket, client_address):
#     while True:
#         data = input("Enter the message:")
#         client_socket.sendall(data.encode())

# def server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind(('localhost', 5160))
#         print("Peer1 is listening.")
#         server_socket.listen(1)
#         client_socket, client_address = server_socket.accept()
#         # client_thread = threading.Thread(target=handle_client, args=(server_socket,client_socket,client_address))
#         # client_thread.start()
#         handle_client(client_socket, client_address)

# def client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         client_socket.connect(('localhost', 1234))
#         print("Connected to Peer1.")
#         while True:
#             data = input("Enter the message:")
#             client_socket.sendall(data.encode())
#             if data == "exit":
#                 break




# Function to handle incoming connections from other peers
def handle_peer(peer_socket, peer_addr):
    print(f"[*] Connected to peer {peer_addr[0]}:{peer_addr[1]}")
    while True:
        try:
            data = peer_socket.recv(1024)
            if not data:
                break
            print(f"Received from {peer_addr[0]}:{peer_addr[1]}: {data.decode()}")
        except Exception as e:
            print("Error:", e)
            break
    print(f"[*] Connection to peer {peer_addr[0]}:{peer_addr[1]} closed")
    peer_socket.close()

# Function to start listening for incoming connections from other peers
def start_listener(port):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('0.0.0.0', port))
    listen_socket.listen(5)
    print(f"[*] Listening on port {port}")

    peer_socket, peer_addr = listen_socket.accept()
    peer_handler = threading.Thread(target=handle_peer, args=(peer_socket, peer_addr))
    peer_handler.start()

# Function to connect to another peer
def connect_to_peer(peer_ip, peer_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.settimeout(10000)
        client_socket.connect((peer_ip, peer_port))
        print(f"[*] Connected to peer {peer_ip}:{peer_port}")
        while True:
            message = input("Enter message to send (type 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
        client_socket.close()
    except socket.timeout:
        print("Connection timed out. Peer is not available.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Port for this peer to listen on
    listen_port = 9999

    # Start listening for incoming connections from other peers
    listener_thread = threading.Thread(target=start_listener, args=(listen_port,))
    listener_thread.start()

    # Example: Connect to another peer
    # Replace peer_ip and peer_port with the IP address and port of the peer you want to connect to
    peer_ip = '127.0.0.1'  # Replace with the IP address of the peer you want to connect to
    peer_port = 8888  # Replace with the port of the peer you want to connect to

    connect_thread = threading.Thread(target=connect_to_peer, args=(peer_ip, peer_port))
    connect_thread.start()