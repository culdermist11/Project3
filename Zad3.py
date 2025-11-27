# Zadanie 3

ulice = ["Jegodowa", "Lipowa", "Kwiatowa", "Kasztanova", "Polna"]

def generuj_adresy(ulice):
    adresy = []
    for ulica in ulice:
        for blok in range(1, 6):
            for lokal in range(1, 11):
                adres = f"{ulica} {blok}/{lokal}"
                adresy.append(adres)
    return adresy

adresy = generuj_adresy(ulice)

for adres in adresy:
    print(adres)
