


varosok = ["Budapest", "Debrecen", "Szeged", "Pécs", "Győr"]


bekert_varos = input("Kérem, adja meg a város nevét: ")


if bekert_varos in varosok:
    index = varosok.index(bekert_varos)
    if index < len(varosok) - 1:
        print(f"A következő város: {varosok[index + 1]}")
    else:
        print("Nincs következő város!")
else:
    varosok.append(bekert_varos)
    print(f"A '{bekert_varos}' város hozzáadva a listához.")

print("Aktuális városlista:", varosok)

