from tkinter import *
from tkinter import messagebox
from details import *
mc=Tk()
img1=PhotoImage(file="login.png")
mc.title("Login")
mc.geometry("925x500+300+200")
mc.resizable(False,False)
mc.configure(bg="#fff")
Label(mc,image=img1,bg="white").place(x=50,y=50)
fr=Frame(mc,height=350,width=350,bg="white")
fr.place(x=450,y=70)
login=Label(fr,text="Login in",fg="#A5F1E9",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
login.place(x=100,y=5)
#login
def loginin():
	aa=loginus.get()
	bb=pw.get()
	a=user
	b=pas
	if aa==a and bb==b:
		vk=Tk()
		mc.destroy()
		vk.title("User")

	else:
		messagebox.showwarning("Password Incorrect", "Your Details Does Not Match")

			
def on_enter(e):
	loginus.delete(0, "end")

def on_leave(e):
	name=loginus.get()
	if name=="":
		loginus.insert(0,"Username")

loginus=Entry(fr,width=25,fg="black",bg="white",border=0,font=("Microsoft YaHei UI Light",11))
loginus.place(x=30,y=80)
loginus.insert(0,"Username")
loginus.bind("<FocusIn>", on_enter)
loginus.bind("<FocusOut>", on_leave)
Frame(fr,width=295,height=2,bg="black").place(x=25,y=107)
#pass
def on_enter1(e):
	pw.delete(0, "end")

def on_leave1(e):
	name=pw.get()
	if name=="":
		pw.insert(0,"Password")

pw=Entry(fr,width=25,fg="black",bg="white",border=0,font=("Microsoft YaHei UI Light",11))
pw.place(x=30,y=150)
pw.insert(0,"Password")
pw.bind("<FocusIn>", on_enter1)
pw.bind("<FocusOut>", on_leave1)
Frame(fr,width=295,height=2,bg="black").place(x=25,y=177)
#button
Button(fr,width=39,pady=7,text="Login",fg="white",bg="#57a1f8",font=("Microsoft YaHei UI Light",9),command=loginin).place(x=35,y=204)

mc.mainloop()
