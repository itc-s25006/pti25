#関数で動作するようにします


import random
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    #print(random.choice(kuji))
    return random.choice(kuji)

kekka = omikuji()
print("結果は"+kekka)
