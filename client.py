from socket import *
from _thread import *
from tkinter import *


s = socket((AF_INET) , SOCK_STREAM)


host = "127.0.0.1"
port = 8000
s.connect((host , port))


root = Tk();
root.title("Client")
root.geometry("400x200")

L1 = Label(root)
L1.grid(row =3 , column=3)

entry = Entry(root , width="40")
entry.grid(row =1 , column =3)


def Clicked():
	message = entry.get()
	s.send(message.encode('utf-8'))
	entry.delete(0 , END)

btn = Button(root , text = "Send" , bg ="Red" , fg = "black" , width =8 , height =1 , command=Clicked)
btn.grid(row=1 , column=4)


def recvThread(s):
	while True:
		L1["text"] = s.recv(1204).decode('utf-8')

start_new_thread(recvThread , (s,))

root.mainloop();