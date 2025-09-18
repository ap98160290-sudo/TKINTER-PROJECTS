import tkinter as tk
def save_data():

    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    d=ent4.get()
    e=ent5.get()
    print(a,b,c,d,e)
    output.config(text="data submitted successfully")


app=tk.Tk()
app.geometry("400x500")
app.title("GOOGLE FORM")
app.config(bg="skyblue")
lbl=tk.Label(app,text="***ENTER YOUR DETAILS***",bg="skyblue",fg="orange",font=("comic sans ms",30,"bold"))
lbl.grid(row=1,column=3,padx=10,pady=20)
# x=tk.Label(app,text="",bg="skyblue")

lbl1=tk.Label(app,text="Full Name",fg="black",bg="skyblue",font=("consolas",25,"italic"))
lbl2=tk.Label(app,text="AGE",fg="black",bg="skyblue",font=("consolas",25,"italic"))
lbl3=tk.Label(app,text="Phone Number",fg="black",bg="skyblue",font=("consolas",25,"italic"))
lbl4=tk.Label(app,text="Email-Id",fg="black",bg="skyblue",font=("consolas",25,"italic"))
lbl5=tk.Label(app,text="Message",fg="black",bg="skyblue",font=("consolas",25,"italic"))


lbl6=tk.Label(app,text=":",fg="black",bg="skyblue",font=("consolas",20,"bold"))
lbl7=tk.Label(app,text=":",fg="black",bg="skyblue",font=("consolas",20,"bold"))
lbl8=tk.Label(app,text=":",fg="black",bg="skyblue",font=("consolas",20,"bold"))
lbl9=tk.Label(app,text=":",fg="black",bg="skyblue",font=("consolas",20,"bold"))
lbl10=tk.Label(app,text=":",fg="black",bg="skyblue",font=("consolas",20,"bold"))

output=tk.Label(app,text="",font=("comic sans ms",20,"italic"),bg="skyblue",fg="red")



ent1=tk.Entry(app,font=("comic sans ms",20,"bold"),bg="yellow",fg="grey")
ent2=tk.Entry(app,font=("comic sans ms",20,"bold"),bg="yellow",fg="grey")
ent3=tk.Entry(app,font=("comic sans ms",20,"bold"),bg="yellow",fg="grey")
ent4=tk.Entry(app,font=("comic sans ms",20,"bold"),bg="yellow",fg="grey")
ent5=tk.Entry(app,font=("comic sans ms",20,"bold"),bg="yellow",fg="grey")

# x.grid(row=0,column=0)
lbl1.grid(row=2,column=0,pady=10)
lbl2.grid(row=3,column=0,pady=10)
lbl3.grid(row=4,column=0,pady=10)
lbl4.grid(row=5,column=0,pady=10)
lbl5.grid(row=6,column=0,pady=10)


lbl6.grid(row=2,column=2,pady=10)
lbl7.grid(row=3,column=2,pady=10)
lbl8.grid(row=4,column=2,padx=10,pady=10)
lbl9.grid(row=5,column=2,pady=10)
lbl10.grid(row=6,column=2,pady=10)
output.grid(row=10,column=3)

ent1.grid(row=2,column=3)
ent2.grid(row=3,column=3)
ent3.grid(row=4,column=3)
ent4.grid(row=5,column=3)
ent5.grid(row=6,column=3)

btn=tk.Button(app,text="SUBMIT",bg="yellow",fg="black",font=("comic sans ms",25,"bold"),activebackground="blue",activeforeground="red",command=save_data)
btn.grid(row=7,column=3,pady=30)


app.mainloop()