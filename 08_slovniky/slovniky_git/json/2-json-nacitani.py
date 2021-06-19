#Je potreba naimportovat modul 'json'
# Prevod mezi retezcem a slovnikem
import json

# Toto je retezec na vice radcich, neda se pristupovat k jednotivym polozkam

json_retezec_kocka = """
{
    "jméno": "Drobek",
    "oblibené_krmivo": "CatFood Premium Deluxe",
    "váha": 11,
    "rasa": "Pouliční směs"
}
"""

# Proto si z json retezce nejprve museim vytvorit slovnik

nacteny_json_kocicka = json.loads(json_retezec_kocka)
nacteny_json_kocicka['odblešena'] = True
print(nacteny_json_kocicka)
