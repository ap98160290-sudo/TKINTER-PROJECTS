# print("Hello, Python in VS Code!")
# print("Hello, Python in VS Code!")

# #CREATE GUI
# #tkinter is a standard GUI (Graphical User Interface) library for Python.
# #It is included with most Python installations, so you don't need to install it separately.

# #config------>bg color
# #Label------->text.
# #ENTRY------->INPUT BOX.
# #BUTTON------>for buttons.
# #font------->font size , font style,font color

# import tkinter as tk
# app=tk.Tk()                 ## Create a new Tkinter window
# app.geometry("600x500")    ## Set the size of the window
# app.title("My First Project")   # Set the title of the window
# app.config(bg="purple")  ## Set the background color of the window

# lbl=tk.Label(app,bg="white",text="hello friends",font =("Arial",33,"bold"))  ## Create a label with specified text and font
# lbl.pack(pady=103,padx=173)   ## Add the label to the window with padding around it
# lbl.config(fg="black")  ## Set the foreground color of the label text

# ent=tk.Entry(app,bg="orange",fg="black",font=("arial",20,"bold"))
# ent.insert(0,"click below")
# ent.pack(pady=80)

# btn=tk.Button(app,text="click here",font=("arial",20,"bold"))   ## Create a button with specified text and font
# btn.pack()  ## Create a button with specified text and font

# app.mainloop()            ## Start the Tkinter event loop to display the window






import tkinter as tk

def calculate_age():
    xy=ent.get()  # Get the input from the entry widget
    age =int(xy)  # Convert the input to an integer
    new_age=2025-age  # Calculate the age based on the input
    show_info.config(text=f"Your age is {new_age}")  # Update the label with the calculated age

app=tk.Tk()
app.geometry("500x600")
app.title("AGE CALCULATOR")
app.config(bg="yellow")
lbl=tk.Label(app,bg="blue",text="CALCULATING AGE",font=("arial",33,"underline"))
lbl.pack(pady=120)

ent=tk.Entry(app,bg="purple",font=("arial",20,"bold"),fg="brown")


ent.pack(pady=20,padx=120)


btn=tk.Button(app,text="click me",font=("arial",33,"underline"),fg="black",bg="white",command=calculate_age)
btn.config(activebackground="orange",activeforeground="black")
btn.pack()

show_info=tk.Label(app,text="",bg="lightblue",font=("arial",20,"bold"))
show_info.pack(pady=20)

app.mainloop()