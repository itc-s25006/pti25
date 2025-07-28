import sklearn.datasets
import matplotlib.pyplot as plt  # ← 修正ここ！

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[0], cmap="Greys")  # ← pltに修正
plt.show()

