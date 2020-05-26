from tkinter import *
import webbrowser

def open_csc421():
	webbrowser.open("https://heat.csc.uvic.ca/coview/course/2020011/CSC421")

def open_csc361():
	webbrowser.open("https://heat.csc.uvic.ca/coview/outline/2020/Spring/CSC/361")

def open_seng330():
	webbrowser.open("https://heat.csc.uvic.ca/coview/outline/2020/Spring/SENG/330")

def open_seng401():
	webbrowser.open("https://heat.csc.uvic.ca/coview/course/2020011/SENG401")

root = Tk()
root.geometry("300x250")
root.configure(background='black')
root.title("Winter 2020 course outlines")

button = Button(root, text="CSC 361", padx=50, pady=20, command = open_csc361)
button1 = Button(root, text="CSC 421", padx=50, pady=20, command = open_csc421)
button2 = Button(root, text="SENG 330", padx=50, pady=20, command = open_seng330)
button3 = Button(root, text="SENG 401", padx=50, pady=20, command = open_seng401)

button.pack()
button1.pack()
button2.pack()
button3.pack()

root.mainloop() 

