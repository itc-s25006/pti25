import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage = (PIL.Image.open(path)
                .rotate(90)
                .transpose(PIL.Image.FLIP_LEFT_RIGHT) #水平方向に反転
                .convert("L")
                .resize((300,300))
                .resize((300,300),resample=0))
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

