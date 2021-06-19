def secti(a, b):
    return a + b

def deleni(a, b):
    return a / b

'''
### Programatori jsou lini, tak na spousteni testu existuje i modul pytest
# je nutne ho nainstalovat
# instalaci provadet v prostredi venv
# je jedno kde jsme ve strukture
# pomoc pip
# python umi moduly i spoustet v pripade...
# python3 -m pip install pytest
# -m rika pythonu ze ma vyhledat modul jmenem pytest
#python3 -m pytest scitani
# pytest am vyhleda vsechny funkce ktere zacinaji slovem test_


### Aby to bylo prehledne, tak se assserty davaji do samostatne Funkce
def test_secti():
    assert secti(2, 3) == 5
def test_secti_jinak():
    assert secti(2, 3) == 4, 'pokus' # pokus je hodnota vyjimky

### Pata varianta zapisu
# Tento zapis umoznuje dat vyjimce hodnotu - tedy nas vlastni text
assert secti(2, 3) == 5
assert secti(2, 3) == 4, 'pokus' # pokus je hodnota vyjimky

### Ctvrty level testovani - assert
# v podsate je to jakoby jednodussi zapis if
assert False # vyhodi chybu
assert True #
assert 1 # nevyhodi vyjimku

assert secti(2, 3) == 5 # if is equal... vyhodi True, v pripade ze to neni equal - vyhodi vyjimku

### Treti level testovani
if secti(6,10) != 15:
    raise Exception('nefunguje to')


### Druy level testovani - ale stale se na nej musim divat
print(secti(6,10))

### Prvni level testovani
while True:
    a = input('')
    a = int(a)
    print(secti(a, a))

'''
