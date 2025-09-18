from currency_converter import CurrencyConverter
import tkinter as tk
app=tk.Tk()
app.geometry("400x360")
a=CurrencyConverter()
def currency():
    amount=float(ent1.get())
    curr1=ent2.get()
    curr2=ent3.get()
    value=a.convert(amount,curr1,curr2)
    output.config(text=f"{amount}{curr1}={value}{curr2}")


app.title("CURRENCY CONVERTER")
app.config(bg="WHITE")



bg_image=tk.PhotoImage(file=r"c:\Users\admin\Desktop\currency_converter_project\abc.png")
bg=tk.Label(app,image=bg_image)
bg.grid(row=0,column=0,rowspan=20, columnspan=10)

lbl1=tk.Label(app,text="***CONVERTER FOR CURRENCY***",bg="WHITE",fg="black",font=("comic sans ms",22,"bold"))
lbl2=tk.Label(app,text="ENTER AMOUNT",bg="WHITE",fg="black",font=("comic sans ms",12,"bold"))
lbl3=tk.Label(app,text="CONVERTING FROM",bg="WHITE",fg="black",font=("comic sans ms",12,"bold"))
lbl4=tk.Label(app,text="CONVERTING TO",bg="WHITE",fg="black",font=("comic sans ms",12,"bold"))
output=tk.Label(app,text="",bg="WHITE",fg="black",font=("consolas",30,"italic"))

ent1=tk.Entry(app,bg="LIGHT GREY",fg="black",font=("consolas",14,"bold"))
ent2=tk.Entry(app,bg="LIGHT GREY",fg="black",font=("consolas",14,"bold"))
ent3=tk.Entry(app,bg="LIGHT GREY",fg="black",font=("consolas",14,"bold"))

lbl1.grid(row=0,column=1)
lbl2.grid(row=5,column=1,pady=40)
ent1.grid(row=5,column=2,padx=10,pady=40)
lbl3.grid(row=6,column=1,padx=10,pady=40)
ent2.grid(row=6,column=2,padx=10,pady=40)
lbl4.grid(row=7,column=1,padx=10,pady=40)
ent3.grid(row=7,column=2,padx=10,pady=40)
output.grid(row=10,column=1,pady=30)


btn=tk.Button(app,text="CONVERT",bg="WHITE",fg="green",font=("comic sans ms",22,"bold"),activebackground="red",activeforeground="blue",command=currency)
btn.grid(row=8,column=4,pady=20)


app.mainloop()





# import os 
# print(os.path.exists("C:/Users/admin/Desktop/practice for project/1.png"))