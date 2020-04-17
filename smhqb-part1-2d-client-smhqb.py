import socket

# parameters

def client_messages(filename,client_socket):
        
	while True:
		if filename == "exit":
			client_socket.send(str.encode(filename))
			data=str(client_socket.recv(1024).decode())
			print(data)
			if(data == "Server connection is closed"):
				break
			else:
				filename=input('send another message  --> ')
				filename=filename.lower()

		elif filename == "weather":
			client_socket.send(str.encode(filename))
			data=str(client_socket.recv(1024).decode())
			print(data)
			filename=input("send another message  -->")
			filename=filename.lower()
		else:
			client_socket.send(str.encode(filename))
			data=str(client_socket.recv(1024).decode())
			print(data)
			filename=input("Enter standard messages -->")
			filename=filename.lower()

def main():
	client_socket=socket.socket()
	client_socket.connect((socket.gethostname(),12345))
	filename=input("Enter message here -->")
	filename=filename.lower()
	client_messages(filename,client_socket)
	client_socket.close()

if __name__== "__main__":
	main()
