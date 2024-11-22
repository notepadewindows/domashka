class valluta():
    def __init__(self):
        self.USD = 41.48
        self.Euro =43.43
while True:
    def konw():
        val = valluta()
        vudir = input("виберіть валюту доллар - U євро - E ")
        grn = int( input("введіть суму "))
        if vudir == "U":
            print("приблизно",round( grn / val.USD), "USD")
        if vudir == "E":
            print("приблизно",round( grn / val.Euro), "євро")
    konw()
