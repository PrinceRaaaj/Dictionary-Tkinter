from bs4 import BeautifulSoup
import requests
from tkinter import messagebox
from tkinter import *



def search(input):
    page = requests.get("https://dictionary.cambridge.org/dictionary/english/"+input)
    soup = BeautifulSoup(page.content, "html.parser")
    des = soup.find(class_="def ddef_d db")
    try:
    	messagebox.showinfo("Cambridge Dictionary Meaning", des.get_text()[0:len(des.get_text())-2])
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