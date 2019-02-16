import struct
from socket import *
import os
import time


def main():

	requestFileData = struct.pack("!Hsb5sb", 1, "a", 0, "octet", 0)
	udpSocket=socket(AF_INET,SOCK_DGRAM)
	udpSocket.sendto(requestFileData,("192.168.1.14",69))
	udpSocket.close()

if __name__ == '__main__':
		main()
	
