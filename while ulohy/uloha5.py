#napíš program, ktorý bude v cykle načítavať slová dovtedy, pokiaľ nezadáte slovo začínajúce sa na písmeno "x". Program vypíše celkový počet znakov všetkých slov okrem posledného slova, začínajúceho sa na x
slovo = input("Napis hocijake slovo:")
slovo = str(slovo)

znaky = len(slovo)

while slovo[0] != "x":
    slovo = input("Napis dalsie slovo:")
    slovo = str(slovo)
    znaky = znaky + len(slovo)
znaky = znaky - 1 #ako odpocitat vsetky znaky?
print("Celkovy pocet znakov je:", znaky)
