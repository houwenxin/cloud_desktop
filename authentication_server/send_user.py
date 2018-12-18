import socket

def send_crinfo(ip,username,password):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (ip, 12001)
	server.connect(server_address)
	server.sendall('create %s %s'%(username,password))
	server.close()

def send_delinfo(ip,username):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (ip, 12001)
        server.connect(server_address)
        server.sendall('delete %s NULL'%(username))
        server.close()
