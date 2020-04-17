
import socket

# import required modules 
import requests, json 
  
# Enter your API key here 
api_key = "826452db8586427f8a08cacac318a514"
  
# base_url variable to store url 
base_url = "https://api.weatherbit.io/v2.0/forecast/daily?city=Kansas"



# parameters
#api.openweathermap.org/data/2.5/forecast/daily?q=Kansas&cnt=3&appid=1eda3204a9b631abba8d6724f5b4c91a

#https://api.weatherbit.io/v2.0/forecast/daily?city=Kansas&key=826452db8586427f8a08cacac318a514&days=3

def bind():
	server_socket=socket.socket()
	server_socket.bind((socket.gethostname(),12345))
	print('listening ...')
	server_socket.listen(1)
	c,addr = server_socket.accept()
	return c

def server_messages(c):
	while True:
		recvdata=str(c.recv(1024).decode())
		recvdata=recvdata.lower()
		if recvdata == "exit":
			print(recvdata)
			c.send(str.encode("Server connection is closed"))
			
			break
		elif recvdata == "weather":
                            print(recvdata)
                            complete_url = base_url + "&key=" + api_key + "&days=3"
                            response = requests.get(complete_url)

                        # python format data 
                            x = response.json()

                            y = x["data"]
                           
                            #print(y)
                            print(y[0]["temp"])
                            str1=""
                            for i in range(3):
                                item=str(y[i]["temp"])+" "
                                str1 += item
                                #str1.join(y[i]["temp"])
                                

                            c.send(str.encode("Next consecutive three days temperature :"+str1+"units:c"))
		else:
			print(recvdata)
			c.send(str.encode(recvdata))
	#c.close()
	
	
def main():
	c=bind()
	
	server_messages(c)
	
	c.close()

if __name__== "__main__":
	main()
