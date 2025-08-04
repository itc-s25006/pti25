def predictDigits(data):
    diggits=sklearn.datasets.load_digits()
    cif = sklearn.datasets.load_digits()
    clf.fit(digits.data,,digits.target)
    n=clf.predict([data])
    textLabel.configure(text = "この画像は"+str(n)+"です！")
