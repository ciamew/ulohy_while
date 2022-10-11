#napíš program, ktorý bude V CYKLE načítavať mená a vypisvať ich dĺžku dovtedy, poikiaľ ako meno nezdáte reťazec "koniec"

meno = input("Napis meno:")
meno = str(meno)

dlzka = 0

while meno != "koniec":
    dlzka = len(meno)
    print("Dlzka mena je:", dlzka)
    meno = input("Napis dalsie meno:")
    meno = str(meno)
print("koniec")