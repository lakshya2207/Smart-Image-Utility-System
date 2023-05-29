from utilities import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog  import *
import tkinter.messagebox as tmsg


root=Tk()
path=""
menul=[]
root.config(bg="#252525")
root.title("Duplicate Image Deleter")
root.geometry("850x450")
root.resizable(width=False, height=False)
def folderc():
        location=askdirectory(title="Select the Folder")
        folderv.set(location)
frame1=LabelFrame(root,text="Selection",bg="#232325",fg="#ffffff",height=165,width=800)
label=Label(root,text="Duplicate Image Deleter",bg="#252525",fg="#ffffff",font="Helvetica 35 bold italic")
label.pack(pady=20)
folderv=StringVar()
l1=Label(root,text="Location of folder having duplicate images :-",font="Helvetica 11",bg="#252525",fg="white").place(x=80,y=120)
foldere=Entry(root,textvariable=folderv,width=80).place(x=83,y=145,height=23)
def take_input():
        
        path=folderv.get()
        ftype=filetype.get()
        dl=[]
        if ftype=="jpg":
                dl=delete_duplicate(path,"jpg")
                dl.append(delete_duplicate(path,"JPG"))
                if dl!=[[]]:
                        tmsg.showinfo("Deletion is successful",f"Following files are deleted \n {dl}")
                else:
                        tmsg.showinfo("Deletion is not successful",f"No duplicate files to Delete !!")
        elif ftype=="png": 
                dl=delete_duplicate(path,"png")
                dl.append(delete_duplicate(path,"PNG"))
                if dl!=[[]]:
                        tmsg.showinfo("Deletion is successful",f"Following files are deleted \n {dl}")
                else:
                        tmsg.showinfo("Deletion is not successful",f"No duplicate files to Delete !!")
        else:
                dl=delete_duplicate(path,ftype)
                if dl!=[[]]:
                        tmsg.showinfo("Deletion is successful",f"Following files are deleted \n {dl}")
                else:
                        tmsg.showinfo("Deletion is not successful",f"No duplicate files to Delete !!")
l2=Label(root,text="/",fg="white",font="Helvetica 24",bg="#252525").place(x=570,y=136)
b1=Button(root,text="Browse...",command=folderc,relief="ridge").place(x=590,y=144,height=23)
filetype=StringVar()
filetype.set("type")
Label(root,text="Select the filetype :",font="Helvetica 11",bg="#232325",fg="#ffffff").place(x=80,y=182)
radio = Radiobutton(root, text="jpeg",activebackground="#252525", activeforeground="white", selectcolor="#252525",bg="#232325",fg="#ffffff",variable=filetype, value="jpeg").place(x=470,y=182)
radio = Radiobutton(root, text="jpg",activebackground="#252525", activeforeground="white", selectcolor="#252525",bg="#232325",fg="#ffffff",variable=filetype, value="jpg").place(x=250,y=182)
radio = Radiobutton(root, text="png",activebackground="#252525", activeforeground="white", selectcolor="#252525",bg="#232325",fg="#ffffff", variable=filetype, value="png").place(x=360,y=182)
submit=ttk.Button(root,text="Delete Duplicate Images",command=take_input).place(x=360,y=225)
frame1.pack()

root.mainloop()
