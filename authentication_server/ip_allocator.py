#! /usr/bin/python
#coding=utf-8

import os

def find_ip():
	#find ip in ipallocator
        f = open("ipallocator","r+")
	readline = f.readlines()
	f.close()
	f = open("ipallocator","w")
	i = 0
	real_ip = 0
	for eachline in readline:	
		eachline = eachline.strip('\n')
		ip_flag = eachline.split(":")[0]
		ip = eachline.split(":")[1]
		#利用标识符ocp（占用中）和usb(可使用)来区分可用ip
		if(real_ip == 0):
			if eachline.startswith("ocp"):
				i += 1
				f.seek(0,1)
				f.write(ip_flag+":"+ip+os.linesep)
				continue
		#找到ip后，利用每行字符并且定位行数，然后找到ocp所在的那一行并且把flag改成ocp
			elif eachline.startswith("usb"):
				ip_flag = "ocp"
                       		f.seek(0,1)
                        	f.write(ip_flag+":"+ip+os.linesep)   
				real_ip = ip
				continue
		elif(real_ip != 0):
			f.seek(0,1)
			f.write(ip_flag+":"+ip+os.linesep)
	f.close()
	print real_ip
	return real_ip

def recycle_ip(ip):
	 f = open("ipallocator","r+")
         readline = f.readlines()
	 f.close()
	 f = open("ipallocator","w")
         i = 0
         #readline = readline.strip('\n')
         for eachline in readline:
                eachline = eachline.strip('\n')
                # ip_flag = readline.split(":")[1]
		ip_flag = eachline.split(":")[0]
		check_ip = eachline.split(":")[1]
		#找到ip后再将标识符改回usb
                if(check_ip != ip):
			f.seek(0,1)
			f.write(ip_flag+":"+check_ip+os.linesep)
			continue
		elif(check_ip == ip):
			ip_flag = "usb"
			f.seek(0,1)
			f.write(ip_flag+":"+check_ip+os.linesep)
			continue
         f.close()

'''
if __name__ == "__main__":
#	ip = find_ip()
#	print ip
	recycle_ip("192.168.32.11")
	recycle_ip("192.168.200.68")
'''
