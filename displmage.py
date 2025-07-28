import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)  # ← タイプミス修正
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData  # ← これ大事！参照を持たせて画像が消えないように

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command=openFile)  # ← bth → btn に直したよ
btn.pack()

imageLabel = tk.Label()
imageLabel.pack()

root.mainloop()
