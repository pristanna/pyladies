# Soutezni verze piskvorku na 3. 5. 2018

from random import randrange

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, cislo_policka, symbol):

    cislo_policka2 = cislo_policka + 1
    pole_vlevo= pole[:cislo_policka]
    pole_vpravo= pole[cislo_policka2:]
    return pole_vlevo + symbol + pole_vpravo

def tah_hrace(pole, symbol2):

    # Funkce na zjisteni druhého symbolu
    if symbol2 == "x":
        symbol = "o"
    elif symbol2 == "o":
        symbol = "x"
    else:
        print("Nastala nějáka chyba při zjištování symbolu")

    # Kontrola záporných a velkých čísel
    while True:
        cislo_policka=int((input("Na kterou pozici chces hrat? Zadej 0-19: ")))
        if cislo_policka < 0 or cislo_policka > 19:
             print ("Zadej číslo 0-19. Tzn. číslo, které není záporné a je meší nebo rovno 19.")
        # Kontrola obsazených políček
        elif cislo_policka in obsazena_policka(pole, symbol, symbol2):
             print ("Toto pozice už je obsazená, zadej volnou pozici.\nObsazená políčka jsou tato: " + str(obsazena_policka(pole, symbol, symbol2)).strip('[]'))
             # Jak převádět list na stringy: https://www.decalage.info/en/python/print_list, strip odstraní z obou stran zadané znaky
        else:
            return tah(pole, cislo_policka, symbol2)


def obsazena_policka_pc(pole, symbol):
    # Odpověd 59 - https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
    obsazena_policka_pc = ( [pos for pos, char in enumerate(pole) if char == symbol])
    return obsazena_policka_pc

def obsazena_policka_hrac(pole, symbol2):
    # Odpověd 59 - https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
    obsazena_policka_hrac = ( [pos for pos, char in enumerate(pole) if char == symbol2])
    return obsazena_policka_hrac

def obsazena_policka(pole, symbol, symbol2):
    obsazena_policka_hrac = ( [pos for pos, char in enumerate(pole) if char == symbol2]) # Odpověd 59 - https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
    obsazena_policka_pc = ( [pos for pos, char in enumerate(pole) if char == symbol])
    return obsazena_policka_hrac + obsazena_policka_pc

def tah_pocitace(pole, symbol):

    # Funkce na zjisteni druhého symbolu
    if symbol == "x":
        symbol2 = "o"
    elif symbol == "o":
        symbol2 = "x"
    else:
        print("Nastala nějáka chyba při zjištování symbolu")

    # Pocatecni inicializace promenne
    index = 0
    index2 = 0

    # Pokud policko neni volne, opakuj od bodu 1 - https://stackoverflow.com/questions/12828771/how-to-go-back-to-first-if-statement-if-no-choices-are-valid
    if symbol in pole:
        while True:

            if len(obsazena_policka_pc(pole, symbol)) > index:
                #print("len vetsi nez pole")
                # Zkousim jestli je volna pozice vpravo od pc symbolu
                cislo_policka = obsazena_policka_pc(pole, symbol)[index] + 1
                if cislo_policka not in obsazena_policka(pole, symbol, symbol2) and cislo_policka < 20:
                    return tah(pole, cislo_policka, symbol)

                # Zkousim jestli je volna pozice vlevo od pc symbolu
                cislo_policka = obsazena_policka_pc(pole, symbol)[index] - 1
                if cislo_policka not in obsazena_policka(pole, symbol, symbol2) and cislo_policka < 20:
                    return tah(pole, cislo_policka, symbol)

                index += 1

            # Modul pro braneni
            if symbol2 in pole and len(obsazena_policka_hrac(pole, symbol2)) > index2:
                    #print("Jsem tam kde jsem chtela", obsazena_policka_hrac(pole, symbol2))
                    # Zkousim jestli je volna pozice vpravo od hracova symbolu
                    cislo_policka = obsazena_policka_hrac(pole, symbol2)[index2] + 1
                    if cislo_policka not in obsazena_policka(pole, symbol, symbol2) and cislo_policka < 20:
                        return tah(pole, cislo_policka, symbol)

                    elif cislo_policka in obsazena_policka(pole, symbol, symbol2) and cislo_policka < 20:
                        # Zkousim jestli je volna pozice vlevo od hracova symbolu
                        cislo_policka = obsazena_policka_hrac(pole, symbol2)[index2] - 1
                        if cislo_policka not in obsazena_policka(pole, symbol, symbol2) and cislo_policka < 20:
                            return tah(pole, cislo_policka, symbol)
                    index2 += 1

            else:
                print("len mensi nez pole, jedeme nahodne")
                while True:
                    cislo_policka = randrange(len(pole))
                    if cislo_policka not in obsazena_policka(pole, symbol, symbol2):
                        return tah(pole, cislo_policka, symbol)           # break ukončí cyklus a pokračuje dalším krokem funkce, kdežto return ukončí celou funkcí a navrátí nějákou hodnotu
                                                                                # Nepoužívat break a return dohromady
                    #print ("Netrefil jsem volnou pozici, hraji znovu")

    elif symbol not in pole:
        #print ("o not in pole")
        while True:
            cislo_policka = randrange(len(pole))
            if cislo_policka not in obsazena_policka(pole, symbol, symbol2):
                return tah(pole, cislo_policka, symbol)
            #print ("Netrefil jsem volnou pozici, hraji znovu")
    else:
        return "Asi nastala nejaka chyba"


def piskvorky1d():
    pole = "-" * 20
    na_tahu = "x"

    while True:
        if na_tahu == "x":
            pole = tah_hrace(pole, "x")
            na_tahu = "o"
        elif na_tahu == "o":
            pole = tah_pocitace(pole, "o")
            na_tahu = "x"

        vysledek = vyhodnot(pole)
        print(pole)

        if vysledek != "-":
            if vysledek == "!":
                print("Remiza! {}".format(pole))
            elif vysledek == "x":
                print("Vyhravas nad pocitacem! {}".format(pole))
            elif vysledek == "o":
                print("Bohuzel, pocitac vyhral. {}".format(pole))
            else:
                raise ValueError("Nepripustny vysledek hry '{}'".format(vysledek))
            return


piskvorky1d()
