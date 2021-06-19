# zamen(retezec, pozice, znak)
# zamen('valec', 2, 'j')

retezec=(input("Zadej slovo:\n"))
pozice=int((input("Zadej pozici pismena, ktere chces zamenit:\n")))
znak=(input("Zadej nova pismena:\n"))

#def zamen(retezec, pozice, znak):
pozice = pozice - 1 # aby to bylo lidske...
pozice2 = pozice + 1
retezec1= retezec[:pozice]
retezec2= retezec[pozice2:]
print(retezec1 + znak + retezec2)
