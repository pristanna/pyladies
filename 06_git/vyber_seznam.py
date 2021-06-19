retezec = 'příšerně žluťoučký kůň úpěl ďábelské ódy na bílý měsíc'      # používá se na kontrolu diaritiky
seznam = retezec.split(" ")
print(seznam)

print(seznam[0])
print(seznam[1:3])
print(seznam[1:-2])
print(seznam[-0])
print(seznam[-1])
print(seznam[::2])

##### Manipulace seznamu
# všechny přepisují ten původní seznam!!!
# Pokud chci ten původní zachovat, potřebuji si vytvořit kopii toho původího
# Občas kopie nestačí, je potřeba použít deep copy, ta nám zaručí, že seznam se opravdu zkopíruje a né že se do proměnné vloží jen odkaz na ten původní seznam, což se může stát
##### Vkládání

print("Vkládání")
upraveny_seznam = seznam + ['AAA', 'BBB']
print(upraveny_seznam)
upraveny_seznam.append('CCC')               # Přidám jedné položky na konec seznamu
print(upraveny_seznam)
upraveny_seznam.insert(0, 'První')          # Vložení na určitý index
print(upraveny_seznam)
upraveny_seznam.extend(['DDD', 'EEE'])      # Přidání více položek na konec seznamu

##### Nahrazování

upraveny_seznam[1:3] = ['nahrazeny']        # Nahrazení určité položky
print(upraveny_seznam)

###### Řazení
# prvky musí být stejného typu
# abeceda - nejprve řadí velká písmena a pak velká

upraveny_seznam.sort()
print(upraveny_seznam)
novy_seznam = upraveny_seznam.sort()
print(novy_seznam)
#upraveny_seznam.sort(reverse = True)       # Reverse order
#print(upraveny_seznam)

##### Mazání
#

del upraveny_seznam[1]
print(upraveny_seznam)
print(upraveny_seznam.pop())                # Smaže posledné hodnotu
print(upraveny_seznam)
print(upraveny_seznam.remove('AAA'))        # Zde vybíráme prvek, který chceme smazat
print(upraveny_seznam)
