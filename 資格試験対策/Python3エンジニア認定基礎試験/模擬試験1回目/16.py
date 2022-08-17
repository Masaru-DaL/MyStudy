def shop(name, 【A】):
    print("flowershop:", name)
    for arg in arguments:
        print(arg)
    print("**Recommended**")
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

shop("Iris","Open: 9:30 am","Close: 10:30 pm","Monday and holidays are closed.",bouquet="Sunflower",plants="Pachira",dried="Rose")

[実行結果]
flowershop: Iris
Open: 9:30 am
Close: 10:30 pm
Monday and holidays are closed.
**Recommended**
bouquet : Sunflower
dried : Rose
plants : Pachira
