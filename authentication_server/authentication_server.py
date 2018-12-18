#! /usr/bin/python
import os
import socket
import SocketServer
import threading
import encryptionAES
import user_operation
import ip_allocator
import time
import send_user

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12000

class ForkingHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		recept = self.request.recv(1024)
		if recept == '1': #login mode
	                print "Waiting to be connected..."
	                transfer = self.request.recv(1024).split(":")
        	        identity = transfer[0]
                	username = transfer[1]
                	password = transfer[2]
                	print identity
                	print username
                	print password
			if(identity == '1'):
                    		if(encryptionAES.certificate(username, password)[0] == True):
                        		self.request.send("Correct")
                        		ip = ip_allocator.find_ip()
					send_user.send_crinfo(ip,username,password)
                        		time.sleep(1)
                        		self.request.send(ip)
					print "%s uses %s" %(os.getpid(),ip)
					temp = self.request.recv(1024)
					if(temp == 'down'):
						ip_allocator.recycle_ip(ip)
						print "%s is recycled" %ip
						send_user.send_delinfo(ip,username)

#                        		while(1):
#                                		time.sleep(5)
#                                		self.request.sendall("ARE YOU OK")
#                                		check = self.request.recv(1024)
#                                		if(check == "still in use"):
#                                        		print "PID:%s IP:%s is still in use" %(os.getpid(),ip)
#                                		else:
#							print "PID:%s IP:%s is down"%(os.getpid(),ip)
#                                        		break
#                        		ip_allocator.recycle_ip(ip)
                    		else:
                        		self.request.send("Wrong")

			elif(identity == '2'):
                    		(iv, ciphertext) = encryptionAES.encrypt(password)
                    		answer = user_operation.create_new_user(username, iv, ciphertext)
                    		if(answer == True):
                        		self.request.send("Log up successfully")
                    		elif(answer == False):
                        		self.request.send("The username has already been logged up")
                    		else:
                        		self.request.send("Invalid username or password")

                #delete account
                	elif(identity == '3'):
                   		response = user_operation.delete_user(username, password)
                   		if(response == True):
	                       		self.request.send("Correct")
                   		else:
        	               		self.request.send("Wrong")
		elif recept == '2':	#recycle ip
			ip = self.request.recv(1024)
			ip_allocator.recycle_ip(ip)
			print "%s recycled" %ip
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
