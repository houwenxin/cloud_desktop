import os
import socket
import SocketServer
import threading
import user_process

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12001

class ForkingHandler(SocketServer.BaseRequestHandler):
        def handle(self):
		recept = self.request.recv(1024)
		username = recept.split(" ")[1]
		password = recept.split(" ")[2]
		print username
		print password
		if(recept.startswith("create")):
			print("Create temp user...")
			user_process.create_user(username,password)
		elif(recept.startswith("delete")):
			print("Delete temp user...")
			user_process.delete_user(username)	

class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer, ):
        pass

def main():
	print("Waiting to be connected...")
        server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingHandler)
        server_thread = threading.Thread(target=server.serve_forever)
        #server_thread.setDaemon(True)
        server_thread.start()

if __name__ == '__main__':
        main()
