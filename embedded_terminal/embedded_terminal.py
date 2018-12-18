#! /usr/bin/python
# coding=utf_8
import os
import socket
import time

port = 12000

def client(host, port, identity, username, password):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (host, port)
	print "Connecting to %s port %s" %server_address
	server.connect(server_address)
	
	try:
            #determin the operation
            #identity = raw_input("1 for login, 2 for logup, 3 for delete:")
            #server.sendall(identity)
	    #username=raw_input("Username: ")
	    #server.sendall(username)
	    #password=raw_input("Password: ")
            #server.sendall(password)
            server.send('1')
            time.sleep(3)
            server.sendall(identity+":"+username+":"+password)
            response = server.recv(1024)

            #When user tries to log in
            if(identity == '1'):
                if(response == "Correct"):
			print "Serching for usable IP..."
			ip = server.recv(1024)
                        os.system("rdesktop %s -u %s -p %s" % (ip,username,password))
			server.send("down")
#			while(True):
#				checker = server.recv(1024)
#				if(checker == "ARE YOU OK"):
#					server.sendall("still in use")
                elif(response == "Wrong"):
                    print "Wrong username or password"

            #When user tries to log up
            elif(identity == '2'):
                print response

            #When user tries to delete an account
            elif(identity == '3'):
                if(response == "Correct"):
                    print "The account is deleted"
                else:
                    print "The username doesn't exist or the password is wrong"
        except socket.errno, e:
	    print "Socket error: %s" %str(e)
	except Exception, e:
	    print "Other exception: %s" %str(e)
	finally:
	    print"Closing..."
	    server.close()

#if __name__ == '__main__':
#	client(port)
