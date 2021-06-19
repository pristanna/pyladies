def prazdny_obrazec():
    seznam = []
    for radek in range(5):
        seznam.append(5 * ['0'])
    return(seznam)

def tisknout_obrazec(seznam):
    for radek in seznam:
        print(' '.join(radek))
    print()

# Vypis prazdny prazdny_obrazec

tisknout_obrazec(prazdny_obrazec())

seznam = prazdny_obrazec()
seznam[0:2] = [ 5 * 'X', 5 * 'X']
tisknout_obrazec(seznam)

seznam_2 = prazdny_obrazec()
seznam_2[2][1:4] = ['X', 'X', 'X']
tisknout_obrazec(seznam_2)

seznam_3 = prazdny_obrazec()

    # Toto vytvori tupple, varati nam vice hodnot nez jednu, muzeme ukladat do vice promennych najednou, jsou to vlastne n-tice, vyuziva se v pripadech kdy je pevne dane poradi

for radek in seznam_3:                              # Iteruje postupne po vsech radcich
    for cislo_r, radek in enumerate(seznam_3):       # Iteruje postupne po   vsech radcich
        for cislo_b, bunka in enumerate(radek):
            if cislo_b in [0, 4] or cislo_b == cislo_r:
                seznam_3[cislo_r][cislo_b] = 'X'
tisknout_obrazec(seznam_3)

print('Pocet X v prostrednim radku: ', seznam_3[2].count('X'))
print('Pocet 0 v prostrednim radku: ', seznam_3[2].count('0'))

# github vecny optimista pyladies




# Spocitat kolik X a O je u jednotlivych obrazcu
