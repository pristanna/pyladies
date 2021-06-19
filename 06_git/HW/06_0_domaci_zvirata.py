seznam = ['pes', 'kočka', 'andulka', 'králík', 'had']

# 01 Napiš funkci, která vrací jména domácích zvířat(zadaných argumentem), která jsou kratší než 5 písmena

def delka(seznam):
    for x in seznam:
        if len(x) > 5:
            return x
    else:
        return "Nejaka chyba"

print(delka(seznam))

# 02 Napiš funkci, která vrátí jména domácích zvířat, která začínají na k

def zacatek_slova(seznam):
    for x in seznam:
        if x[0] == "k":
            return x
    else:
        return "Nejaka chyba"

print(zacatek_slova(seznam))

# 03 Napiš funkci, která dostane slovo a zjistí, jestli je v seznamu domácích zvířasint

def obsahuje(seznam, slovo):
    if slovo in seznam:
        return True
    else:
        return False

print(obsahuje(seznam, 'králík'))
print(obsahuje(seznam, 'klokan'))

# Napiš funkci, která dostane dva seznamy jmen zvířat a vrátí tři seznamy
# a) zvířata, která jsou v obou seznamech
# b) zvířata, která jsou jen v jednom seznamu
# c) zvířata, která jsou v jen druhém seznamu

def vrat_tri_seznamy(seznam, seznam2):
    spojeny_seznam = seznam + seznam2
    return spojeny_seznam

seznam2 = ['pes', 'chameleon', 'kočka', 'rybička', 'had']

print(vrat_tri_seznamy(seznam, seznam2))

# 05 Napiš program, který seřadí seznam domácích zvířat podle abecedy
print(seznam)

def abecedne(seznam):
    serazeny_seznam = seznam.sort()
    return serazeny_seznam
    # ??? Tady mi to z nějákého důvodu změní ten původní seznam i přesto, že si ho ukládám do nové proměnné serazeny_seznam
print(abecedne(seznam))

# 06 - Had byl pyšný.... seřaď prvky tak že ignoruješ první písmeno

def abecedne2(seznam):

    seznam.sort(key=lambda x:x[1])
    return seznam
    # ??? Tady mi to z nějákého důvodu změní ten původní seznam i přesto, že si ho ukládám do nové proměnné serazeny_seznam
print(abecedne2(seznam))
