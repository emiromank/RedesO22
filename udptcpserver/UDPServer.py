import socket
from datetime import datetime

serverPort = 12000
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print("the server is ready with ip")


while 1:
	option, clientAddress = serverSocket.recvfrom(2048)

	message, clientAddress = serverSocket.recvfrom(2048)
	print(clientAddress)
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)


	if option.decode()=='a':
		now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		serverSocket.sendto(now.encode(), clientAddress)
	elif option.decode()=='b':
		ss=str(modifiedMessage.decode().count('S'))
		serverSocket.sendto(ss.encode(), clientAddress)
	else:
		print('invalido')
