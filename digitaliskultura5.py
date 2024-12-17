import random

magassagok = [random.randint(0, 9) for _ in range(30)]

meredek_felfele = 0
meredek_lefele = 0

for i in range(1, len(magassagok)):
    if magassagok[i] >= magassagok[i - 1] + 2:
        meredek_felfele += 1
    elif magassagok[i] <= magassagok[i - 1] - 2:
        meredek_lefele += 1

print(f"Magasságok: {magassagok}")
print(f"Meredek szakaszok felfelé: {meredek_felfele}")
print(f"Meredek szakaszok lefelé: {meredek_lefele}")