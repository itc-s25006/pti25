import tkinter as tk

def displabel():
    lbl.configure(text="さようなら")

root = tk.Tk()
root.geometry("200x100")

lbl=tk.Label(text="lebel")
btn = tk.Button(text="プッシュ",command = displabel)

lbl.pack()
btn.pack()
tk.mainloop()
