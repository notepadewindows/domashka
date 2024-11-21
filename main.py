import time
def tim ():
    start = input("старт S")
    if start == "S":
        timestart = time.time()
        end = input("кінець E")
        if end == "E":
            timeend = time.time()
            timee = round(timeend - timestart)
            print("функція працювала",timee,"секунд")
tim()
