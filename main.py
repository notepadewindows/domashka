from random import randint
class easy_coder :
    def __init__(self):
        self.coder1 = 5*6+3*9-15
        self.coder2 = 11*4/2+8
        self.coder3 = 13*3+2
        self.coder4 = 15*2+7-1/2
        self.coder5 = 17*3+3
easy_coder = easy_coder()
def cod ():
    key = randint(1,5)
    number = int(input("введіть число"))
    if key == 1:
        finish = easy_coder.coder1 + number
        print(finish)
        print("ваш ключ", key)
    if key == 2:
        finish = easy_coder.coder2 + number
        print(finish)
        print("ваш ключ", key)
    if key == 3:
        finish = easy_coder.coder3 + number
        print(finish)
        print("ваш ключ", key)
    if key == 4:
        finish = easy_coder.coder4 + number
        print(finish)
        print("ваш ключ", key)
    if key == 5:
        finish = easy_coder.coder5 + number
        print(finish)
        print("ваш ключ", key)
cod()