class cat:
    def __init__(self):
        self.happines = 20
        self.hp = 10
cat = cat()
while cat.happines < 60:
    print("рівень щастя", cat.happines, "хп", cat.hp)
    vubir = input("пограти з хазяїном (P)""поїсти (E)")
    if vubir == "P":
        cat.happines += 10
    if vubir == "E":
        cat.hp += 5
print("ви щасливий кіт")