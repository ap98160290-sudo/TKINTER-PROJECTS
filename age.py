import tkinter as tk
def calculate_age():
    xy=ent.get()
    age=int(xy)
    new_age=2025-age
    abc.config(text=f'YOU ARE {new_age} YEARS OLD')
app=tk.Tk()
app.title("age calculator")
app.geometry("400x350")


lbl=tk.Label(app,text="*CALCULATING AGE*",bg="light blue",fg="black",font=("arial",25,"italic"))
lbl.pack(padx=20,pady=20)

ent=tk.Entry(app,bg="white",fg="black",font=("arial",45,"bold"))
ent.pack(padx=20,pady=30)

btn=tk.Button(app,text="click here",bg="blue",fg="black",font=("arial",20,"bold"),command=calculate_age)
btn.config(activebackground="red",activeforeground="black")
btn.pack(padx=30,pady=20)

abc=tk.Label(app,text="",font=("arial",25,"bold"),bg="blue",fg="black")
abc.pack(padx=30,pady=20)
app.mainloop()