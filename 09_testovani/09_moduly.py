### Moduly

# Hotove moduly je mozne importovat....
print(math) # vypise mi cestu k modulu

# .. je mozno importovat i jen casti modulu
from math import pi
print(pi)

# casti modulu je mozno importovat i pod jinym nazvem - ale to se vetsinou nedela
from math import pi as cislo_policka
print(cislo_pi)

### Vytvareni vlastnich modulu

# vytvorit soubor louka.py:

'''
>>> import louka
>>> print(louka.barva_travy)
zelena

'''
# python ma seznam cest, kde moduly vyhledava
# tyto cesty zjistim takto:

'''
>>> import sys
>>> print(sys.path)
['', 'C:\\Users\\Anna\\Dropbox\\pyladies\\venv_hp\\Scripts\\python36.zip', 'C:\\
Users\\Anna\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 'C:\\Users\\Anna
\\AppData\\Local\\Programs\\Python\\Python36\\lib', 'C:\\Users\\Anna\\AppData\\L
ocal\\Programs\\Python\\Python36', 'C:\\Users\\Anna\\Dropbox\\pyladies\\venv_hp'
, 'C:\\Users\\Anna\\Dropbox\\pyladies\\venv_hp\\lib\\site-packages']
'''

# !!! Nevytvaret si vlastni moduly se jmenem

# Pokud nactu modul ze slozky, tak se v te slozce ze ktere jsem ho importovala vytvori adresar __pycache__

print(louka.secti(3,4))
