
jmeno=input("Jake je tve jmeno?\n")
prijmeni=input("Jake je tve prijmeni?\n")

def inicialy(jmeno, prijmeni):
    print("Tvoje inicialy jsou: " + jmeno[0].upper() + prijmeni[0].upper()) # Da se pekne kombinovat suffixy a s metodami, upeer neprijima argumenty

inicialy(jmeno, prijmeni)

print("Tve inicialy jsou {}".format("BP")) # Format je lepsi v pripade ze scitame stringu vice
print("Vysledek {} + {} je {}".format(3, 4, 3 + 4)) # Format je lepsi v pripade ze scitame stringu vice
print("Vysledek {prvni_cislo} + {druhe_cislo} je {treti_cislo}".format(prvni_cislo=3,druhe_cislo=4,treti_cislo=5))
print("Ahoj %s"%('Pavlino')) # Toto je stare formatovani retezce... nepouzivat, jen o tom vedet
