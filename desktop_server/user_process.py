import os

def create_user(username,passwd):
	os.system('useradd -d /home/%s %s' %(username,username))
	os.system('echo "%s:%s" | chpasswd' %(username,passwd))
	os.system('mkdir -p /home/%s' %username)
	os.system('chown %s:%s /home/%s' %(username,username,username))

def delete_user(username):
	os.system('userdel -r -f %s' %(username))
'''
if __name__ == '__main__':
	username = raw_input('username: ')
        passwd = raw_input('password: ')
	create_user(username, passwd)
	#delete_user(username)	
'''
