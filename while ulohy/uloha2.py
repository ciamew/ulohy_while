#načítavaj čísla dovtedy, pokiaľ ich súčet nepresiahne hodnotu 100. Program vypíše hodnotu tohto súčtu a aj počet čísel

cislo = input("Zadaj cislo:")
cislo = int(cislo)

sucet = 0
pocet = 0

while (cislo + sucet) < 101:
    pocet += 1
    sucet += cislo
    cislo = input("Zadaj dalsie cislo:")
    cislo = int(cislo)
print("Sucet cisel je:", sucet, "Pocet je:", pocet)
