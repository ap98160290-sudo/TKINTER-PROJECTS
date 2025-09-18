from currency_converter import CurrencyConverter
import tkinter as tk
from PIL import Image,ImageTk

a=CurrencyConverter()
def currency():
    try:
        amount=float(ent1.get())
        curr1=ent2.get()
        curr2=ent3.get()
        data=a.convert(amount,curr1,curr2)
        output.config(text=f"{amount}{curr1}={data}{curr2}")
    except ValueError:
        output.config(text="PLEASEE ENTER VALID DATA")
    except Exception as e:
        output.config(text="SOMETHING WENT WRONG,TRY AGAIN.........")
        

app=tk.Tk()
app.geometry("300x300")
app.title("converter for currency")
app.config(bg="white")

img=Image.open(r"C:\Users\admin\Desktop\practice for project   python project\currency_converter_project\ab.png")
img=img.resize((1400,750))
bg_image=ImageTk.PhotoImage(img)
label=tk.Label(app,image=bg_image)
label.grid(row=0,column=0,rowspan=20,columnspan=30)


lbl1=tk.Label(app,text="**CONVERTER FOR CURRENCY**",bg="white",fg="black",font=("comic sans ms",14,"bold"))
lbl2=tk.Label(app,text="ENTER AMOUNT",bg="white",fg="black",font=("comic sans ms",14,"bold"))
lbl3=tk.Label(app,text="CONVERTING FROM",bg="white",fg="black",font=("comic sans ms",14,"bold"))
lbl4=tk.Label(app,text="CONVERTING TO",bg="white",fg="black",font=("comic sans ms",14,"bold"))
output=tk.Label(app,text="",bg="white",fg="red",font=("comic sans ms",18,"bold"))
output.grid(row=9,column=6)

ent1=tk.Entry(app,bg="beige",font=("consolas",15,"italic"))
ent2=tk.Entry(app,bg="beige",font=("consolas",15,"italic"))
ent3=tk.Entry(app,bg="beige",font=("consolas",15,"italic"))

lbl1.grid(row=0,column=3)
lbl2.grid(row=3,column=3)
lbl3.grid(row=4,column=3)
lbl4.grid(row=5,column=3)

ent1.grid(row=3,column=4)
ent2.grid(row=4,column=4)
ent3.grid(row=5,column=4)



btn=tk.Button(app,text="CONVERT",bg="yellow",fg="black",activebackground="red",activeforeground="blue",font=("comic sans ms",20,"italic"),command=currency)
btn.grid(row=7,column=5)










app.mainloop()