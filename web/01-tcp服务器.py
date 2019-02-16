from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", 8899))

serverSocket.listen(5)

print("-----1-----")
clientSocket,clientInfo = serverSocket.accept()

print("-----2-----")
#clientSocket 表示这个新的客户端
#clientInfo 表示这个新的客户端的ip以及port
try:
	while True:
		recvData = clientSocket.recv(1024)
		if len(recvData)>0:
			print("-----3-----")
			print("%s:%s"%(str(clientInfo), recvData))
		else:
			print("[%s]client has closed"%str(clientInfo))
			break
finally:
	clientSocket.close()


serverSocket.close()

