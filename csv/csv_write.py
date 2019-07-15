import csv

filename = 'names.csv'

def printtext():
	global firstName
	global lastName
	string1 = firstName.get()
	string2 = lastName.get()
	with open(filename, mode='a') as f:
		name_writer = csv.writer(f, delimiter=',')
		
		name_writer.writerow([string1,string2])
	print(string1)
	print(string2)

from tkinter import *

class Window(Frame):
	
	def __init__(self, master=None):
		
		Frame.__init__(self, master)
		
		self.master = master
		self.init_window()
		
	def init_window(self):

		self.master.title("User Input")
		
		self.pack(fill=BOTH, expand=1)
		
		menu = Menu(self.master)
		self.master.config(menu=menu)
		
		file = Menu(menu)
		file.add_command(label="Exit", command=self.client_exit)
		
		menu.add_cascade(label="File", menu=file)
		
		edit = Menu(menu)
		


		edit.add_command(label="Undo")
		
		menu.add_cascade(label="Edit", menu=edit)
		
	def client_exit(self):
		exit()


root = Tk()

root.geometry("400x300")


firstName = Entry(root)
firstName.pack()
firstName.focus_set()

lastName = Entry(root)
lastName.pack()

b = Button(root,text='Save',command=printtext)
b.pack(side='bottom')

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
