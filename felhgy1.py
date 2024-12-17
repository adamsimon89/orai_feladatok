
mondatok = []
for szokoz in range(5):
    mondat = input("Írjon be 5 mondatot")
    mondatok.append(mondat)


szokozok_szama = []
for mondat in mondatok:
    szokozok = 0
    for karakter in mondat:
        if karakter == ' ':
            szokozok += 1
    szokozok_szama.append(szokozok)

max_szokoz = -1
max_szokoz_index = -1
for szokoz in range(len(szokozok_szama)):
    if szokozok_szama[szokoz] > max_szokoz:
        max_szokoz = szokozok_szama[szokoz]
        max_szokoz_index = szokoz

print(f"A legtöbb szóközt tartalmazó : {mondatok[max_szokoz_index]}")