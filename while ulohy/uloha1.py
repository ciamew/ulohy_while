#načítavaj čísla dovtedy, pokiaľ nenačítaš číslo väčšie ako 100. Ak sa to stane, program skončí a vypíše celkový počet načítaných čísel

cislo =input("Zadaj cislo:")
cislo = int(cislo)

pocet = 0

while cislo <=100:
    pocet += 1
    cislo = input("Zadaj dalsie cislo:")
    cislo = int(cislo)
print("Pocet nacitanych cisel je:", pocet)