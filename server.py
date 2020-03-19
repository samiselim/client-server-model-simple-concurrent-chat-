from socket import * 
from _thread import *
from tkinter import *


s = socket((AF_INET) , SOCK_STREAM) 

host = "127.0.0.1"
port = 8000

s.bind((host , port))

s.listen(5) 


sessions = []

def Clicked():
	message = "Server : " + entry.get()
	for c in sessions:
		c.send(message.encode('utf-8'))
	entry.delete(0 , END)


def recvThread(c,ad):
	while True:
		L1["text"]= str(ad[1]) +" : " + c.recv(1024).decode('utf-8')
		

while True:
	c , ad = s.accept()
	message = "New connection from " + ad[1]
	for session in sessions:
		session.send(message.encode('utf-8'))
	sessions.append(c)
	start_new_thread(recvThread , (c,ad))

