from tkinter import *
import qrcode

root=Tk()
root.title("Qr generator")
root.geometry("450x450")
root.config(bg="#FF7256")
root.resizable(False,False)

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save(str(name)+".png")


Label(root,text="Name",fg="#fff",bg="#FF7256",font=25).place(x=50,y=160)

Label(root,text="Link",fg="#fff",bg="#FF7256",font=25).place(x=50,y=220)

title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=190)

entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=250)

Button(root,text="Generate",width=20,height=2,bg="#8B2323",fg="white",command=generate).place(x=50,y=320)


root.mainloop()
