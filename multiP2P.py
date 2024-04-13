import socket
import sys
import threading
import os

counter_clients = 0

# Function to handle incoming connections from other peers
def handle_peer(peer_socket, peer_addr):
    print(f"[*] Connected to peer {peer_addr[0]}:{peer_addr[1]}")
    while True:
        try:
            data = peer_socket.recv(1024)
            if not data:
                break
            elif data.decode().lower().startswith('transfer'):
                _, filename = data.decode().split()
                filename = "new"+filename
                print(filename)
                with open(filename, 'wb') as file:
                    while True:
                        chunk = peer_socket.recv(1024)
                        if chunk.endswith(b'END_OF_FILE'):
                            print("Reached End")
                            chunk = chunk[:-len(b'END_OF_FILE')]
                            file.write(chunk)
                            break
                        file.write(chunk)
                print(f"File {filename} received.")
            else:
                print(f"Received from {peer_addr[0]}:{peer_addr[1]}: {data.decode()}")
        except Exception as e:
            print("Error:", e)
            break
    print(f"[*] Connection to peer {peer_addr[0]}:{peer_addr[1]} closed")
    peer_socket.close()

# Function to start listening for incoming connections from other peers
def start_listener(port):
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.bind(('localhost', port))
    while True:
        listen_socket.listen(5)
        peer_socket, peer_addr = listen_socket.accept()
        peer_handler = threading.Thread(target=handle_peer, args=(peer_socket, peer_addr))
        peer_handler.start()

# Function to connect to another peer
def connect_to_peer(peer_ip, peer_port, timeout=5):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.settimeout(timeout)  # Set timeout for connection attempt
        client_socket.connect((peer_ip, peer_port))
        print(f"[*] Connected to peer {peer_ip}:{peer_port}")
        while True:
            message = input("Enter message to send (type 'exit' to quit): ")
            client_socket.sendall(message.encode())
            if message.lower() == 'exit':
                break
            #if the message is to transfer a file
            if message.lower().startswith('transfer'):
                _, filename = message.split()
                if os.path.isfile(filename):
                    with open(filename, 'rb') as file:
                        chunk = file.read(1024)
                        while chunk:
                            client_socket.send(chunk)
                            chunk = file.read(1024)
                    client_socket.send(b'END_OF_FILE')
                else:
                    print(f"File {filename} not found.")
        client_socket.close()
    except socket.timeout:
        print(f"Connection to peer {peer_ip}:{peer_port} timed out. Peer may not be reachable.")
        client_socket.close()
    except ConnectionRefusedError:
        print(f"Connection to peer {peer_ip}:{peer_port} refused. Peer may not be turned on or not reachable.")
        client_socket.close()
    except Exception as e:
        print("Error:", e)
        client_socket.close()


if __name__ == "__main__":
    # Port for this peer to listen on
    # listen_port = 8888
    try:
        listen_port = int(sys.argv[1])
    except:
        listen_port = int(input("Enter the listening port number: "))
    # Start listening for incoming connections from other peers
    listener_thread = threading.Thread(target=start_listener, args=(listen_port,))
    listener_thread.start()

    # Example: Connect to another peer
    # Replace peer_ip and peer_port with the IP address and port of the peer you want to connect to
    peer_ip = 'localhost'  # Replace with the IP address of the peer you want to connect to
    peer_port = int(input("\nEnter the peer port number: "))
    # peer_port = 9999  # Replace with the port of the peer you want to connect to

    connect_thread = threading.Thread(target=connect_to_peer, args=(peer_ip, peer_port))
    connect_thread.start()