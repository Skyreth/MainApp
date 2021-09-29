from tkinter import *

Xsize = 500
Ysize = 250

tk = Tk()

# init

tk.title("Main")
tk.geometry("500x250")
tk.minsize(Xsize, Ysize)
tk.maxsize(Xsize, Ysize)
tk.config(background='#861D07')

label_title = Label(tk, text="Welcome to my Main App", font=("Verdana", 25), fg="#8C1813")
label_title.pack(expand="YES")

saisi = Entry(tk, width=10)
saisi.grid(row=0, sticky='ew')

tk.mainloop()
