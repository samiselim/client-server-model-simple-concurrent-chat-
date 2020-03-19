from socket import * 
from _thread import *
from tkinter import *


s = socket((AF_INET) , SOCK_STREAM) 

host = "127.0.0.1"
port = 8000

s.bind((host , port))

s.listen(5) 

root = Tk();
root.title("Server")
root.geometry("400x200")

L1 = Label(root)
L1.grid(row =3 , column=3)

entry = Entry(root , width="40")
entry.grid(row =1 , column =3)

sessions = []

def Clicked():
	message = "Server : " + entry.get()
	for c in sessions:
		c.send(message.encode('utf-8'))
	entry.delete(0 , END)

btn = Button(root , text = "Send" , bg ="Red" , fg = "black" , width =8 , height =1 , command=Clicked)
btn.grid(row=1 , column=4)

def recvThread(c,ad):
	while True:
		L1["text"]= str(ad[1]) +" : " + c.recv(1024).decode('utf-8')
		
def mainTread(s):
	while True:
		c , ad = s.accept()
		sessions.append(c)

		L1["text"] = "new connection from "+ str(ad[1])
		start_new_thread(recvThread , (c,ad))
start_new_thread(mainTread , (s,))

root.mainloop()
