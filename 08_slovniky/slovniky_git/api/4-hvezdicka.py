import requests

with open('token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

# Kazda akce kterou chci udelat potrebuje jinou adresu - zjistim v napovede k API dane stranky
# Kazda akce kterou chci udelat je potreba jiny prikaz
# Dokumentace k ulozeni repozitare k oblibenym
# https://developer.github.com/v3/activity/starring/#star-a-repository



stranka = requests.?
stranka.raise_for_status()
