from random import randrange

'''
while True:
    print("Cislo je", randrange(10000))
    print("(Pockej nez se pocitac unavi...)") # vitiskne i uvozovky
'''

#odpoved=(input("Co mas rad? "))

#while odpoved != "python":
while True:
    odpoved = input("Rekni Aaaa\n")
    if odpoved == "Aaaa":
        print("Flus! Aaaaaahahaha")

        reakce = input("Jak chces reagovat?")

        if reakce == "Flus!":
            print("Ty jsi ale vychcanek!!!")
        break
    print("Spatne, zkus to znovu!")

print("Hotovo, ani to nebolelo")
