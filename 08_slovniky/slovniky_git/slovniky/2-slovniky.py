#Slovniky - Sklada se z dvojic klic-hodnota
    #Napr. Vek -> 30
    #Jmeno -> 'Jana'
    #OblibenaBarva - > 'Modra'

osoba = {
    'Jmeno': 'Jana',
    'Vek': 30,
    'OblibenaBarva': 'Modra',
    'Vyska': 180,
}

print(osoba)
osoba['Vek']

#K polozkam se nepristupuje pres ciselny index, ale klic
print('Jmeno osoby je {}'.format(osoba['Jmeno']))
print('Vek osoby je {}'.format(osoba['Vek']))
print('Oblibena barva osoby je {}'.format(osoba['OblibenaBarva']))

#Kdyz pristoupime k neexistujicimu klici, nastane chyba KeyError
#tuto chybu je mozne osetrit, ale to budeme brat az pozdeji
print('Barva oci osoby je {}'.format(osoba['barva_oci']))

#Polozky lze menit
osoba['Jmeno'] = 'Honza'

#Nove polozky lze pridavat
osoba['barva_oci'] = 'Zelena'

#Polozky lze i odebirat
# del slovnik[klic]
del osoba['Vek']
print(osoba)
