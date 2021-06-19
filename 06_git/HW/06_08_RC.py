rc = input("Zadej rodné číslo ve formátu YYMMDD/XXXX: \n")

def format(rc):
    while True:
        if  len(rc) == 11 and rc[0:6].isdigit() and rc[6:7] == "/" and rc[7:11].isdigit():
            print("Vaše rodné číslo je: ", rc)
            break
        else:
            rc = input("Špatně zadané rodné číslo. Zadej rodné číslo ve formátu YYMMDD/XXXX: ")

def delitelnost(rc):
    rc_cisla = int(rc[0:6] + rc[7:11])
    if rc_cisla % 11 == 0:
        print("Vaše rodné číslo je správně - je dělitelné 11")
    else:
        print("Vaše rodné číslo není správě, musí být dělitelné 11")

def datum_narozeni(rc):

    if rc[2] == "5" or rc[2] == "6":
        mesic = "0" + str(int(rc[2:4]) - 50)
    elif rc[2] == "0" or rc[2] == "1":
        mesic = rc[2:4]
    else:
        print("Neco je spatne")

    rok = rc[0:2]
    den = rc[4:6]

    print("Vaše datum narození je: ", den, mesic, rok)

def pohlavi(rc):
    if rc[2] == "5" or rc[2] == "6":
        print("žena")
    elif rc[2] == "0" or rc[2] == "1":
        print("muž")
    else:
        print("Neco je spatne")
        
format(rc)
delitelnost(rc)
datum_narozeni(rc)
pohlavi(rc)
