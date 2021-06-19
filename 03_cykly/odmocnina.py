from math import sqrt

cislo=float(input("Zadej číslo které chceš odmocnit: "))

# Osetrit si vstup od uzivatele, aby nam skript nespadl

if cislo < 0:
    print("Zadejte kladne cislo, zaporne nelze odmocnit")
elif cislo > 0:
    print("Odmocnina cisla ", cislo, "je ", sqrt(cislo))
