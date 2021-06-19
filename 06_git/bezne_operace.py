retezec = 'příšerně žluťoučký kůň úpěl ďábelské ódy na bílý měsíc'      # používá se na kontrolu diaritiky
seznam = retezec.split(" ")

print(seznam)
print(len(seznam))                          # Vypsání délky seznamu
print(seznam.count('NA'))                   # Nutno zadat co chci spočítat, vrati index
print(seznam.index('žluťoučký'))            # Vyhodi nam index na kterem se nachazi
#print(seznam.index('slon'))                # Vyhodi chybu protoze tam hledane slovo neni

if ('slon' in seznam):                      # Vhodne je nejprve si zjistit jestli tam vubec to slovo je
    index = (seznam.index('slon'))
    print(seznam.index('slon'))

print('_'.join(seznam))                     # Spojeni prvku seznamu pomoci symbolu
