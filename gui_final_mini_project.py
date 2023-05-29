from tkinter import *
from tkinter import ttk
from subprocess import call
from PIL import Image,ImageTk
import PIL

def click_qr():
    call(["python", "gui_qrscan.py"])
def click_imgcomp():
    call(["python", "gui_imgcomp.py"])
def click_text():
    call(["python", "gui_textextracter.py"])
def click_dup():
    call(["python","gui_dup.py"])


root=Tk()
root.title("Smart Image Utility System")
root.geometry("900x501")
root.config(bg="#102e36")
root.resizable(width=False, height=False)
label=ttk.Label(text="Smart Image Utility System",font="Helvetica 35 bold italic",background="#102e36",foreground="white").pack(pady=50)
f1=Frame(background="#102e36")


img1 = Image.open("ico1.png")
img1 = img1.resize((120,130), PIL.Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(img1)

img2 = Image.open("ico2.png")
img2 = img2.resize((120,130), PIL.Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(img2)

img3 = Image.open("ico3.png")
img3 = img3.resize((120,130), PIL.Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(img3)

img4 = Image.open("ico4.png")
img4 = img4.resize((120,130), PIL.Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(img4)


b1=ttk.Button(f1,command=click_dup,image=photo1).pack(side=LEFT,pady=0,padx=20,ipady=40,ipadx=22)
b2=ttk.Button(f1,command=click_text,image=photo2).pack(side=LEFT,pady=0,padx=20,ipady=40,ipadx=22)
b3=ttk.Button(f1,command=click_qr,image=photo3).pack(side=LEFT,pady=0,padx=20,ipady=40,ipadx=22)
b4=ttk.Button(f1,command=click_imgcomp,image=photo4).pack(side=LEFT,pady=0,padx=20,ipady=40,ipadx=22)
#b1=Button(f,text="Duplicate \nImage Deleter",image=img,relief=GROOVE).pack(anchor=CENTER,side=LEFT,pady=20,padx=20,ipady=65,ipadx=25)
f1.pack()

f2=Frame(background="#102e36")
bt1=Button(f2,command=click_dup,text="Duplicate \nImage Deleter",font="Lucida 15 bold",bg="#102e36",fg="white",relief=FLAT).pack(side=LEFT,pady=0,padx=20,ipady=40,ipadx=14)
bt2=Button(f2,command=click_text,text="Text\nExtracter",font="Lucida 15 bold",bg="#102e36",fg="white",relief=FLAT).pack(side=LEFT,pady=0,padx=18,ipady=40,ipadx=35)
bt4=Button(f2,command=click_qr,text="Image\nCompressor",font="Lucida 15 bold",bg="#102e36",fg="white",relief=FLAT).pack(side=RIGHT,pady=0,padx=20,ipady=40,ipadx=20)
bt3=Button(f2,command=click_imgcomp,text="QR Code\nScanner",font="Lucida 15 bold",bg="#102e36",fg="white",relief=FLAT).pack(side=RIGHT,pady=0,padx=21,ipady=40,ipadx=35)
#b1=Button(f,text="Duplicate \nImage Deleter",image=img,relief=GROOVE).pack(anchor=CENTER,side=LEFT,pady=20,padx=20,ipady=65,ipadx=25)
f2.pack()
root.mainloop()