def shop(name, *argsY, **argsX):
    print("flowershop:", name)
    keys = sorted(argsX.keys())
    for kw in keys:
        print(kw, ":", argsX[kw])
    for Y in argsY:
        print(Y)

shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")

