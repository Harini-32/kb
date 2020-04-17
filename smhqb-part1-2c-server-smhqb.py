import os
import socket
from _thread import *

	
def threaded_client(connection):
    #connection.send(str.encode('Welcome to the Server\n'))
    while True:
            data = connection.recv(2048).decode('utf-8')
        

            if data == "exit":
                print(data)
                reply = 'Server connection is closed'
                connection.sendall(str.encode(reply))
                
            else:
                print(data)
                reply = 'Server Says: ' + data
                if not data:
                    break
                connection.sendall(str.encode(reply))
            
		
        
    connection.close()



def main():
    server_socket=socket.socket()
    ThreadCount = 0
    try:
        server_socket.bind((socket.gethostname(),1234))
    except socket.error as e:
        print(str(e))
    print('Waitiing for a Connection..')
    server_socket.listen(1)
    while True:
        c,addr = server_socket.accept()
        print('Connected to: ' + addr[0] + ':' + str(addr[1]))
        start_new_thread(threaded_client, (c, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    server_socket.close()

	
if __name__== "__main__":
	main()
