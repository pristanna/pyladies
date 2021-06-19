strana = int(input("Zadej stranu ctverce: ")) 	# Funkce int nebere desetinna cisla
pi = 3.14 					# pouzivaji se desetinne tecky
polomer = float(input("Zadej polomer kruhu: ")) # Funkce float umi i desetinna cisla

# Toto je jednoradkovy komentar

"""Toto 
je 
viceradkovy
komentar"""

if strana <= 0:
    print("Strana ani polomer nesmi byt zaporne cislo ani nula")
else:
    print("Ctverec o strane ", strana, "ma obvod:", 4*strana, "cm")
    print("Ctverec o strane ", strana, "ma obsah:", strana*strana, "cm")

if polomer <= 0:
    print("Polomer nesmi byt zaporne cislo ani nula")
else:
    print("Obvod kruhu o polomeru", polomer, "je", 2*pi*polomer, "cm")
    print("Obsah kruhu o polomeru", polomer, "je", 2*polomer*polomer, "cm")

# Python2 predchozi text vypise vcetne zavorek a uvozovek, Python3 ho vypise bez zavorek a uvozovek - tzn. spoustet jako python3 
