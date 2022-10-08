import socket
serverName = '127.0.0.1' #input('ip=  ')
serverPort = 12000

clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
opc=input("Escoge tu opcion:\n  a.Fecha y hora actual\n  b.Cantidad de 's' en la oracion\n  :")
clientSocket.sendto(opc.encode(),(serverName, serverPort))

message=input("Frase en minusculas : ")
clientSocket.sendto(message.encode(),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Frase en mayusculas:  ",modifiedMessage.decode())

eleccion, serverAddress = clientSocket.recvfrom(2048)

if opc=='a':
	print("\nFecha: ", eleccion.decode())
elif opc=='b':
	print("\nCantidad de 's' en tu oracion: ", eleccion.decode())
else:
	print("Tu opcion es invalida")

clientSocket.close()
