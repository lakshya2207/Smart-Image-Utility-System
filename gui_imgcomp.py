from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
from utilities import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Image Compressor")
def browse():
    file_path = askopenfilename()
    entry1.set(file_path)
def execute():
    comp=compress(entry1.get())
    tmsg.showinfo("Image Compressor","Compressed succsessfully")
label1 = Label(root,text="Image Compressor",font="Helvitica 36 bold italic",background="#252525",foreground="#ffffff",pady="30").pack()

frame1=LabelFrame(root,text="Selection",bg="#232325",fg="#ffffff",height=190,width=800)
root.geometry("900x500")
root.config(bg='#252525')
root.resizable(width=False, height=False)
label2 = Label(root, text="Enter the path of the Image you want to compresss",background="#252525",foreground="#ffffff",font="Helvitica 12 ").place(x=80,y=170)

entry1 = StringVar()
entry2 = Entry(root,textvariable=entry1,width="82",borderwidth="2",).place(x=80,y=205,height="25")

label3 = Label(root,text="/",bg="#252525",fg="#ffffff",font="helvitica 21 ").place(x=585,y=200)

b1=Button(root,text="Browse...",command=browse,relief="ridge").place(x=610,y=205,height=23)
submit=ttk.Button(root,text="Compress",command=execute).place(x=400,y=260)
frame1.pack()

root.mainloop()