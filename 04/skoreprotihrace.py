# napiste funkci, ktera vrati hlasku na zaklade zadaneho skore

hrac = input("Napis typ hrace, spoluhrac nebo protihrac: ")
skore = int(input("Zadej skore: "))

def vrat_hlasku(typ_hrace, skore):
    if typ_hrace == "protihrac":
        if skore >= 100:
            print("zatracene")
            # return "zatracene" # toto mi nefunguje... nevypise to nic, pokud misto nepouziju print na konci print(vrat_hlasku())
        elif skore < 100:
            print("perfektni")
        else:
            print("Asi si nezadal cislo...")
    elif typ_hrace == "spoluhrac":
        if skore > 100:
            print("perfektni")
        elif skore <= 100:
            print("zatracene")
        else:
            print("Asi si nezadal cislo...")
    else:
        print("spatny argument")

print("Vysledek druhe funkce je: " + str(vrat_hlasku(hrac, skore))) # je nutne to nedriv prevest na string, jinak to hodi chybu


#### Druha verze s return

print("Druha verze s return")

def vrat_hlasku2(typ_hrace, skore):
    if typ_hrace == "protihrac":
        if skore >= 100:
            return "zatracene"
            # return "zatracene" # toto mi nefunguje... nevypise to nic, pokud misto nepouziju print na konci print(vrat_hlasku())
        elif skore < 100:
            return "perfektni"
        else:
            return "Asi si nezadal cislo..."
    elif typ_hrace == "spoluhrac":
        if skore > 100:
            return "perfektni"
        elif skore <= 100:
            return "zatracene"
        else:
            return "Asi si nezadal cislo..."
    else:
        return "spatny argument"

print("Vysledek druhe funkce je: " + vrat_hlasku2(hrac, skore))
