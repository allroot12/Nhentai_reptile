import tkinter as tk
import N
from tkinter import filedialog

window = tk.Tk()
window.title("my window")
window.geometry("300x150")

Lurl = tk.Label(window,text="url")
Lurl.pack()
Eurl = tk.Entry(window)
Eurl.pack()

Lpath = tk.Label(window,text="path")
Lpath.pack()
Vartext = tk.StringVar()
Epath = tk.Entry(window,textvariable=Vartext)
Epath.pack()

def path_set():
    global Vartext
    Vartext.set(filedialog.askdirectory())

Bpath = tk.Button(window,text="文件路径",command=path_set)
Bpath.place(x=225,y=62)

def send():
    url = Eurl.get()
    path = Epath.get()
    N.N(url,path)


Bstart = tk.Button(window,text="start",command=send)
Bstart.pack()

window.mainloop()