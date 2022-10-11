#napíš program, ktorý bude načítavať čísla dovtedy pokiiaľ nezadáte nulu. Na záver program vypíše aritmetický priemer týchto čísel. Nulu do priemeru nezahrňte
cislo = input("Zadaj cislo:")
cislo = int(cislo)

pocet = 1
sucet = cislo

while cislo != 0:
    cislo = input("Zadaj dalsie cislo alebo 0:")
    cislo = int(cislo)
    pocet += 1
    sucet += cislo
ap = sucet / (pocet-1)
ap = round(ap, 2)
print("Aritmeticky priemer je:", ap)