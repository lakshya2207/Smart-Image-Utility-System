from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from utilities import scanqrcode
import webbrowser
import tkinter.messagebox as tmsg


root = Tk()
root.title("QR Code Scanner")
def browse():
    file_path = askopenfilename()
    entry1.set(file_path)
    #print(f"The Path of the Image is:{file_path}")

def execute():
    file_path = entry1.get()
    qr = scanqrcode(file_path)
    if qr!="QR Code not detected":
        t= Text(root, state='disabled', width=35, height=8,font="Helvetica 10",bg="#232323",fg="white")
        t.place(x=150,y=300)
        t.configure(state='normal')
        t.insert("end",qr)
        def copy():
                root.clipboard_append(qr)
        def openinbr():
            webbrowser.open(qr, new=2)
        b1=ttk.Button(root,text="Copy to clipboard",command=copy).place(x=550,y=340)
        b2=ttk.Button(root,text="Open in Browser",command=openinbr).place(x=550,y=380)
    else:
        tmsg.showinfo("Qr Code","QR Code not detected")
root.geometry("850x460")
root.config(bg='#252525')
root.resizable(width=False, height=False)
label1 = Label(root,text="QR Code Scanner",font="Helvitica 36 bold italic",background="#252525",foreground="#ffffff").pack(pady="20")

frame1=LabelFrame(root,text="Selection",bg="#232325",fg="#ffffff",height=165,width=800)
label2 = Label(root, text="Enter the path of the Image to scan the QR Code",font="Helvetica 11",bg="#252525",fg="white").place(x=80,y=125)
entry1 = StringVar()
entry2 = Entry(root,textvariable=entry1,width=80).place(x=83,y=155,height=23)

l2=Label(root,text="/",fg="white",font="Helvetica 24",bg="#252525").place(x=570,y=146)
b1=Button(root,text="Browse...",command=browse,relief="ridge").place(x=590,y=154,height=23)
submit=ttk.Button(root,text="SCAN",command=execute).place(x=360,y=220)
frame1.pack()

root.mainloop()