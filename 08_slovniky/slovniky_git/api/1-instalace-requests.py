#Musis instalovat knihovnu Requests, ktera umoznuje komunikaci pres internet:
#Nezapomen instalaci provest ve virtualnim prostredi!
# python -m pip install requests
# requests je nazev toho co instaluju

import requests

# stažení stránky
stranka = requests.get('https://github.com')

# ověření, že dotaz proběhl v pořádku
stranka.raise_for_status() # Toto vrací None, muze ale vratit i nejaky chybovy kod, ktery je pote mozno nejakym zpusobem osetrit

# vypsání obsahu
print(stranka.text)
