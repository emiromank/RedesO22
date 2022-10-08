import socket
from datetime import datetime

serverPort=12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(3)

option=''

print("Listo servidor TCP")

while 1:
	connectionSocket, addr= serverSocket.accept()
	option=connectionSocket.recv(1024).decode()

	sentence=connectionSocket.recv(1024)
	capSentence=sentence.decode().upper()
	connectionSocket.send(capSentence.encode())

	if option=='a':
		now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		print(now)
		connectionSocket.send(now.encode())
	elif option=='b':
		ss=str(capSentence.count('S'))
		connectionSocket.send(ss.encode())
	else:
		print('invalido')
	#connectionSocket.close()
