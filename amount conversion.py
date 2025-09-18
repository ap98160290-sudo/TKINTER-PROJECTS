import tkinter as tk
from currency_converter import CurrencyConverter
a=CurrencyConverter()
def currency():
    try:

        amount=float(ent3.get())
        cur1=ent.get().upper()
        cur2=ent2.get().upper()
        data=a.convert(amount,cur1,cur2)
        lbl5.config(text=f"{amount}{cur1}={data:.2f},{cur2}",font=("comic sans ms",25,"bold"),bg="grey",fg="RED")
    except ValueError:
        lbl5.config(text="X Please enter valid number")
    except Exception as e:
        lbl5.config(text="X Something Went Wrong,try again .")
app=tk.Tk()
app.geometry("500x360")
app.title("CURRENCY CONVERTER")
app.config(bg="GREY")


lbl5=tk.Label(app,text="")


lbl=tk.Label(app,text="CONVERT CURRENCY",bg="GREY",fg="black",font=("consolas",30,"bold"))


lbl3=tk.Label(app,text="ENTER AMOUNT",bg="grey",fg="black",font=("comic sans ms",15,"bold"))


lbl1=tk.Label(app,text="CONVERT IT FROM",bg="grey",fg="black",font=("comic sans ms",15,"bold"))


lbl2=tk.Label(app,text="CONVERT IT TO",fg="black",bg="grey",font=("comic sans ms",15,"bold"))


ent=tk.Entry(app,bg="light GREY",fg="black",font=("comic sans ms",15,"bold"))

ent2=tk.Entry(app,bg="light GREY",fg="black",font=("comic sans ms",15,"bold"))

ent3=tk.Entry(app,bg="light GREY",fg="black",font=("comic sans ms",15,"bold"))



lbl5.grid(row=8,column=4)
lbl.grid(row=1,column=4,pady=20)
lbl3.grid(row=4,column=3)
lbl1.grid(row=5,column=3)
lbl2.grid(row=6,column=3)
ent.grid(row=5,column=4)
ent2.grid(row=6,column=4)
ent3.grid(row=4,column=4)

btn=tk.Button(app,text="click here to convert",bg="grey",fg="blue",font=("comic sans ms",16,"italic"),activebackground="red",activeforeground="green",command=currency)

btn.grid(row=7,column=4,pady=10)


app.mainloop()