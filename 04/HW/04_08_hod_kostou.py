from random import randrange

hrac1=""
hrac2=""
hrac3=""
hrac4=""
hraci = [hrac1, hrac2, hrac3, hrac4]

for hrac_cislo in hraci:

    cislo = randrange(1,7)
    hrac = str(cislo)

    while cislo < 6:
        cislo = randrange(1,7)
        hrac = hrac + str(cislo)
        hrac_cislo = hrac
        print(hrac_cislo)
    else:
        print("je to jinak")

print("Konec cyklu" + hrac1 + hrac2 + hrac3 + hrac4)
print([hraci])
