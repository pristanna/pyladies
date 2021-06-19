# -*- coding: UTF-8 -*-
# 1-D piškvorky se hrají na řádku s dvaceti políčky.
# Hráči střídavě přidávají kolečka (o) a křížky (x), třeba:
# 1. kolo: -------x------------
# 2. kolo: -------x--o---------
# 3. kolo: -------xx-o---------
# 4. kolo: -------xxoo---------
# 5. kolo: ------xxxoo---------
# Hráč, která dá tři své symboly vedle sebe, vyhrál.

# Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek, a vrátí jednoznakový řetězec
# podle stavu hry:
# "x" – Vyhrál hráč s křížky (pole obsahuje xxx)
# "o" – Vyhrál hráč s kolečky (pole obsahuje ooo)
# "!" – Remíza (pole neobsahuje -, a nikdo nevyhrál)
# "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)

from random import randrange

def vyhodnot(herni_pole):
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif "-" not in herni_pole:
        return "!"
    else:
        return "-"

# Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o), a vrátí
# herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici.
# Hlavička funkce by tedy měla vypadat nějak takhle:
# def tah(pole, cislo_policka, symbol):
# "Vrátí herní pole s daným symbolem umístěným na danou pozici"
# ...

def tah(herni_pole, cislo_policka, symbol):

    cislo_policka2 = cislo_policka + 1
    herni_pole_vlevo= herni_pole[:cislo_policka]
    herni_pole_vpravo= herni_pole[cislo_policka2:]
    return herni_pole_vlevo + symbol + herni_pole_vpravo

# Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát,
# a vrátí herní pole se zaznamenaným tahem hráče.
# Funkce by měla odmítnout záporná nebo příliš velká čísla, a tahy na obsazená políčka. Pokud uživatel
# zadá špatný vstup, funkce mu vynadá a zeptá se znova.

def obsazena_policka(herni_pole):
    obsazena_policka_x = ( [pos for pos, char in enumerate(herni_pole) if char == "x"]) # Odpověd 59 - https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
    obsazena_policka_o = ( [pos for pos, char in enumerate(herni_pole) if char == "o"])
    return obsazena_policka_x + obsazena_policka_o

def tah_hrace(herni_pole):
    symbol = "x"

    # Kontrola záporných a velkých čísel
    while True:
        cislo_policka=int((input("Na kterou pozici chces hrat? Zadej 0-19: ")))
        if cislo_policka < 0 or cislo_policka > 19:
             print ("Zadej číslo 0-19. Tzn. číslo, které není záporné a je větší než 19.")
        # Kontrola obsazených políček
        elif cislo_policka in obsazena_policka(herni_pole):
             print ("Toto pozice už je obsazená, zadej volnou pozici.\nObsazená políčka jsou tato: " + str(obsazena_policka(herni_pole)).strip('[]'))
             # Jak převádět list na stringy: https://www.decalage.info/en/python/print_list, strip odstraní z obou stran zadané znaky
        else:
            return tah(herni_pole, cislo_policka, symbol)

# Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí
# herní pole se zaznamenaným tahem počítače.
# Použij jednoduchou náhodnou „strategii”:
# 1. Vyber číslo od 0 do 19
# 2. Pokud je dané políčko volné, hrej na něj
# 3. Pokud ne, opakuj od bodu 1
# Hlavička funkce by tedy měla vypadat nějak takhle:
# def tah_pocitace(pole):
# "Vrátí herní pole se zaznamenaným tahem počítače"
# ...

def obsazena_policka_pc(herni_pole):
    # Odpověd 59 - https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
    obsazena_policka_o = ( [pos for pos, char in enumerate(herni_pole) if char == "o"])
    return obsazena_policka_o

def tah_pocitace(herni_pole):
    symbol = "o"
    # Pokud policko neni volne, opakuj od bodu 1 - https://stackoverflow.com/questions/12828771/how-to-go-back-to-first-if-statement-if-no-choices-are-valid
    index = 0

    if "o" in herni_pole:
        #print ("o in pole")
        while True:
            if len(obsazena_policka_pc(herni_pole)) > index:
                #print("len vetsi nez pole")
                cislo_policka = obsazena_policka_pc(herni_pole)[index] + 1          # Nutno přidat kontrolu, aby PC nemohl dát symbol na pozici 20....tzn mimo hrací pole
                if cislo_policka not in obsazena_policka(herni_pole):
                    return tah(herni_pole, cislo_policka, symbol)
                index += 1
                #print ("Netrefil jsem volnou pozici, hraji znovu")

            else:
                #print("len mensi nez pole, jedeme nahodne")
                while True:
                    cislo_policka = randrange(len(herni_pole))
                    if cislo_policka not in obsazena_policka(herni_pole):
                        return tah(herni_pole, cislo_policka, symbol)           # break ukončí cyklus a pokračuje dalším krokem funkce, kdežto return ukončí celou funkcí a navrátí nějákou hodnotu
                                                                                # Nepoužívat break a return dohromady
                    #print ("Netrefil jsem volnou pozici, hraji znovu")

    elif "o" not in herni_pole:
        #print ("o not in pole")
        while True:
            cislo_policka = randrange(len(herni_pole))
            if cislo_policka not in obsazena_policka(herni_pole):
                return tah(herni_pole, cislo_policka, symbol)
            #print ("Netrefil jsem volnou pozici, hraji znovu")
    else:
        return "Asi nastala nejaka chyba"


# Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem, a střídavě volá funkce tah_hrace a
# tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze.
# Nezapomeň kontrolovat stav hry po každém tahu.

def piskvorky1d():
    herni_pole = "-" * 20
    na_tahu = "x"

    while True:
        if na_tahu == "x":
            herni_pole = tah_hrace(herni_pole)
            na_tahu = "o"
        elif na_tahu == "o":
            herni_pole = tah_pocitace(herni_pole)
            na_tahu = "x"

        vysledek = vyhodnot(herni_pole)
        print(herni_pole)

        if vysledek != "-":
            if vysledek == "!":
                print("Remiza! {}".format(herni_pole))
            elif vysledek == "x":
                print("Vyhravas nad pocitacem! {}".format(herni_pole))
            elif vysledek == "o":
                print("Bohuzel, pocitac vyhral. {}".format(herni_pole))
            else:
                raise ValueError("Nepripustny vysledek hry '{}'".format(vysledek))
            return


piskvorky1d()
