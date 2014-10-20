#!/usr/bin/python                                                               


import sys
from socket import inet_aton
import struct




if __name__ == '__main__':
	try:
		iplist=sys.argv[1]
		saveFile=sys.argv[2]
		f = open(iplist,"r")			 		
		lines = f.readlines()
		new = list(set(lines))
		new2=sorted(new, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])
		save=open(saveFile,"w")
		save.writelines(new2)
		
	except IndexError:
		print 'Usage: %s <ipList file> <outputfile>' % sys.argv[0]
		sys.exit(-1)