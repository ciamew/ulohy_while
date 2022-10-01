meno = input("Zadaj meno alebo koniec:")
while meno != "koniec":
    dlzka = len(meno) #len returns the number of items in an object
    print("Dlazka mena je ", dlzka)
    meno = input("Zadaj meno alebo koniec: ")
else:
    print("Koniec.")