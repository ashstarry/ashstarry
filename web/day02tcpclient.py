from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(("192.168.1.14",30000))

clientSocket.send(b"hahahaah")

clientSocket.close()