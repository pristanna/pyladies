from math import pi

print(pi)
				# pouzivaji se desetinne tecky
polomer = float(input("Zadej polomer kruhu v centimetrech: ")) # Funkce float umi i desetinna cisla

if polomer <= 0:
    print("Polomer nesmi byt zaporne cislo ani nula")
else:
    print("Obvod kruhu o polomeru", polomer, "je", 2 * pi * polomer, "cm")
    print("Obsah kruhu o polomeru", polomer, "je", 2 * polomer * polomer, "cm")

# Python2 predchozi text vypise vcetne zavorek a uvozovek, Python3 ho vypise bez zavorek a uvozovek - tzn. spoustet jako python3
