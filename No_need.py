#code for client creation
'''
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5160))
'''

#code for server creation
'''
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5160))
'''

#client code for sending data
'''
data = "Hello! World"
client_scoet.send(data.encode())
'''

#server code for receiving data
'''
data = server_socket.recv(1024).decode()
'''
