import tkinter as tk
app=tk.Tk()
app.geometry("600x500")
app.title("GOOGLE FORM")
app.config(bg="light green")

x=tk.Label(app,text="")



lbl=tk.Label(app,text="Name",font=("arial",15,"italic"),bg="black",fg="white")
lbl1=tk.Label(app,text="Age",font=("arial",15,"italic"),bg="black",fg="white")
lbl2=tk.Label(app,text="Phone",font=("arial",15,"italic"),bg="black",fg="white")
lbl3=tk.Label(app,text="Mail",font=("arial",15,"italic"),bg="black",fg="white")
lbl4=tk.Label(app,text="Message",font=("arial",15,"italic"),bg="black",fg="white")




lbl5=tk.Label(app,text=":",font=("arial",15,"bold"),fg="black")
lbl6=tk.Label(app,text=":",font=("arial",15,"bold"),fg="black")
lbl7=tk.Label(app,text=":",font=("arial",15,"bold"),fg="black")
lbl8=tk.Label(app,text=":",font=("arial",15,"bold"),fg="black")
lbl9=tk.Label(app,text=":",font=("arial",15,"bold"),fg="black")




ent=tk.Entry(app,bg="skyblue",font=("arial",20,"bold"),fg="brown")
ent1=tk.Entry(app,bg="skyblue",font=("arial",20,"bold"),fg="brown")
ent2=tk.Entry(app,bg="skyblue",font=("arial",20,"bold"),fg="brown")
ent3=tk.Entry(app,bg="skyblue",font=("arial",20,"bold"),fg="brown")
ent4=tk.Entry(app,bg="skyblue",font=("arial",20,"bold"),fg="brown")




btn=tk.Button(app,text="click me",font=("arial",23,"underline"),fg="black",bg="white")
btn.config(activebackground="red",activeforeground="black")

x.grid(row=0,column=0)
lbl.grid(row=1,column=1)
lbl1.grid(row=2,column=1)
lbl2.grid(row=3,column=1)
lbl3.grid(row=4,column=1)
lbl4.grid(row=5,column=1)
lbl5.grid(row=1,column=2)
lbl6.grid(row=2,column=2)
lbl7.grid(row=3,column=2)
lbl8.grid(row=4,column=2)
lbl9.grid(row=5,column=2)


ent.grid(row=1,column=3,padx=10)
ent1.grid(row=2,column=3,padx=10)
ent2.grid(row=3,column=3,padx=10)
ent3.grid(row=4,column=3,padx=10)
ent4.grid(row=5,column=3,padx=10)


btn.grid(row=6,column=3,pady=20)
app.mainloop()