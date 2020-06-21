from PyDictionary import PyDictionary as pDt
from tkinter import messagebox
from tkinter import *



def search(input): 
	try:
		messagebox.showinfo("Meaning", pDt.meaning(input)['Noun'][0])
	except:
		messagebox.showerror("Meaning not found", "Please type the correct dictionary word")

root = Tk()
root.title("Dictionary")
root.iconbitmap("icon.ico")

frame = LabelFrame(root, padx=25, pady=5)
frame.pack(padx=10, pady=10)


label = Label(frame, text='Enter a word to search in dictionary').grid(row=0, column=0, columnspan=3)
entry = Entry(frame, width=30, borderwidth=5)
entry.grid(row=1, columnspan=3)
label2 = Label(frame, text='').grid(row=2, column=0, columnspan=3)
button = Button(frame, text="Submit", command = lambda: search(entry.get())).grid(row=3, column=1)




root.mainloop()