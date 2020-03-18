from socket import *
from _thread import *

s = socket((AF_INET) , SOCK_STREAM)
host = "127.0.0.1"
port = 8000

s.bind((host , port))

s.listen(5)

def recvThread(c,ad):
	while True:
		x=c.recv(1024).decode('utf-8')
		print(ad[1] , " : " , x)

def sendThread(c,ad):
	while True:
		c.send(input().encode('utf-8'))

while True:
	c , ad = s.accept()
	print("new connection from" , ad[1])
	start_new_thread(sendThread , (c,ad))
	start_new_thread(recvThread , (c,ad))

	