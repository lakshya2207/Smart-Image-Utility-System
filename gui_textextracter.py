from utilities import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog  import *
import tkinter.messagebox as tmsg
import numpy
from PIL import Image
from pytesseract import pytesseract

def text_extracter(image_path):
        import cv2
        path_to_tesseract = r'C:\Users\Lakshya Sharma\AppData\Local\Tesseract-OCR\tesseract.exe'
        img = Image.open(image_path)
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(img)
        #Displaying the extracted text
        return text[:-1]
import os
    
root=Tk()
path=""

root.title("Text Extracter")
root.config(bg="#252525")
root.geometry("850x460")
root.resizable(width=False, height=False)
def imagec():
        location=askopenfilename(title="Select the Image")
        imagev.set(location)
frame1=LabelFrame(root,text="Selection",bg="#232325",fg="#ffffff",height=165,width=800)
label=Label(root,text="Text Extracter",bg="#252525",fg="#ffffff",font="Helvetica 35 bold italic")
label.pack(pady=20)
imagev=StringVar()
l1=Label(root,text="Location of image :-",font="Helvetica 11",bg="#252525",fg="white").place(x=80,y=125)
imagee=Entry(root,textvariable=imagev,width=80).place(x=83,y=155,height=23)
def take_input():
        txt=text_extracter(imagev.get())
        t= Text(root, state='disabled', width=35, height=8,font="Helvetica 10",bg="#232323",fg="white")
        t.place(x=150,y=300)
        t.configure(state='normal')
        t.insert("end",txt)
        def copy():
                root.clipboard_append(txt)

        b1=ttk.Button(root,text="Copy to clipboard",command=copy).place(x=550,y=350)

l2=Label(root,text="/",fg="white",font="Helvetica 24",bg="#252525").place(x=570,y=146)
b1=Button(root,text="Browse...",command=imagec,relief="ridge").place(x=590,y=154,height=23)
submit=ttk.Button(root,text="Extract Text",command=take_input).place(x=360,y=220)
frame1.pack()
root.mainloop()
