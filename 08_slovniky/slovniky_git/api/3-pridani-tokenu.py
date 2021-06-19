import requests

#Nacteme token ze souboru token.txt a ulozime do promenne token
with open('token.txt') as soubor:
    token = soubor.read().strip()

#Vytvorime hlavicky s tokenem
headers = {'Authorization': 'token ' + token}

#K volani API je nutne pridat hlavicky obsahujici token
#Kazda akce kterou chci udelat potrebuje jinou adresu - zjistim v napovede k API dane stranky
#Kazda akce kterou chci udelat je potreba jiny prikaz
stranka = requests.get('https://api.github.com/user', headers=headers)
stranka.raise_for_status()

print(stranka.text)
