import tkinter as tk
from tkinter import messagebox

def show_selection():
    selected = choice.get()
    messagebox.showinfo("Selected Option", f"your option is: {selected}")


root = tk.Tk()
root.title("Option Button ")
root.geometry("300x250")


tk.Label(root, text="choose the one option", font=("Arial", 12)).pack(pady=10)

choice = tk.StringVar()
choice.set("Option 1")  

tk.Radiobutton(root, text="Option 1", variable=choice, value="Option 1").pack(anchor='w')
tk.Radiobutton(root, text="Option 2", variable=choice, value="Option 2").pack(anchor='w')
tk.Radiobutton(root, text="Option 3", variable=choice, value="Option 3").pack(anchor='w')
tk.Radiobutton(root, text="Option 4", variable=choice, value="Option 4").pack(anchor='w')
tk.Button(root, text="Submit", command=show_selection).pack(pady=20)


root.mainloop()