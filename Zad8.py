# Zadanie 8

tekst = "Python jest super"

print("Zerowy: ")
for idx, znak in enumerate(tekst):
    if idx == 0:
        print(znak)


print("Ostatni: ")
for idx, znak in enumerate(tekst):
    if idx == 16:
        print(znak)

print("Co drugi znak: ")
for idx, znak in enumerate(tekst):
    if idx % 2 == 0:
        print(znak)

print("Co trzeci zaczynając od pierwszego: ")
for idx, znak in enumerate(tekst):
    if (idx % 3 == 0 and idx != 0):
        print(znak)

print("Od dziesiątego do ostatniego: ")
for idx, znak in enumerate(tekst):
    if idx >=10:
        print(znak)

print("Wyświetl od końca do początku: ")
for znak in tekst[::-1]:
    print(znak)