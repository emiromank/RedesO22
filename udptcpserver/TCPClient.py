import socket
serverName="127.0.0.1" #input("ip?  ")
serverPort=12000
opc=''

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

opc=input("Escoge tu opcion:\n  a.Fecha y hora actual\n  b.Cantidad de 's' en la oracion\n  :")
clientSocket.send(opc.encode())

sentence=input("Frase en minusculas : ")
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print("Frase en mayusculas:  ", modifiedSentence.decode())
eleccion = clientSocket.recv(1024)

if opc=='a':
	print("\nFecha: ", eleccion.decode())
elif opc=='b':
	print("\nCantidad de 's' en tu oracion: ", eleccion.decode())
else:
	print("Tu opcion es invalida")

#clientSocket.close()
