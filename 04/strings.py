# Jak psat stringy
# Uvozovky
# je jedno, jestli pouzivam jednoduche nebo dvojite, ale je dobre byt konzistentni

# Viceradkove retezce

print("Ahoj \n Jak se mas") # newline
print('''Ahoj
... Jak se mas
... Ja dobre ''')

### Tri moznosti jak zapsat string
# ''
# ""
# '''
# '''
# """
# """

### Kdyz chci vypsat Uvozovky

print("REkl jsem: 'Ahoj'")
print("Rekl jsem: \"Ahoj\"")

### Cesta k odstavci
cesta_k_adresari_dobra = "C:\\Users\\fronkova.pavlina\\nyladies"
#cesta_k_adresari_spatna = "C:\Users\fronkova.pavlina\nyladies" # Interpretuje to jako specialni znaky
print(cesta_k_adresari_dobra)
#print(cesta_k_adresari_spatna)

### S S retezci lze provadet matematicke operace

a = "A"
b = "hoj"
print(a + b)
print(5 * a)

### Retezce

retezec = ("cokolada")
print(retezec[1]) # vrati o
print(retezec[0]) # zacina to od nuly
print(retezec[-1]) # da se k nim pristupovat i od konce... tzn. kdyz chci vedet jaky je posledni znaky

print(len(retezec)) # delka Retezce
print("oko" in retezec) # obsahuje retezec slovo oko?
print("pes" in retezec)
print("pes" not in retezec)

### Porovnavani retezcu a METODY
print("Protihrac" == "protihrac")
print("Protihrac".lower() == "protihrac")

#### Sekani retezcu
print(retezec[:3])
print(retezec[1:3]) # Vcetne prvniho ale bez posledniho <   )
print(retezec[1:5]) # Vcetne prvniho ale bez posledniho <   )
print(retezec[3:]) # od tretiho do konce
print(retezec[-4:]) # vypise ctyri posledni pismena

### Formatovani stringu

print("Tve inicialy jsou {}".format("BP")) # Format je lepsi v pripade ze scitame stringu vice
print("Vysledek {} + {} je {}".format(3, 4, 3 + 4)) # Format je lepsi v pripade ze scitame stringu vice
print("Vysledek {prvni_cislo} + {druhe_cislo} je {treti_cislo}".format(prvni_cislo=3,druhe_cislo=4,treti_cislo=5))
print("Ahoj %s"%('Pavlino')) # Toto je stare formatovani retezce... nepouzivat, jen o tom vedet
