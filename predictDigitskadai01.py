import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# 画像からデータへ変換
def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS)
    numImage = np.asarray(grayImage, dtype=float)
    numImage = 16 - np.floor(17 * numImage / 256)
    numImage = numImage.flatten()
    return numImage

# 予測処理
def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    print("予測 =", n[0])

# 実行部
data = imageToData("2.png")
predictDigits(data)

