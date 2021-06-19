# Kamen nuzky papir
from random import randrange
cislo = randrange(3)

while True:
    tah_cloveka = input("Jaky je tvuj tah - kámen, nůžky, nebo papír? Pokud cheš hru ukončit, zadej konec. Zvol: ")

    if cislo == 0:
        tah_pocitace = "kámen"
    elif cislo == 1:
        tah_pocitace = "nůžky"
    elif cislo == 2:
        tah_pocitace = "papír"
    else:
        print("Nerozumim tvemu tahu - zkus to znovu")

    print("Tvůj tah byl: ", tah_cloveka)
    print("Tah pocitace byl: ", tah_pocitace)

    if tah_cloveka == tah_pocitace:
        print("Remíza\n")
    elif (tah_cloveka == "kámen" and tah_pocitace == "nůžky") or (tah_cloveka == "nůžky" and tah_pocitace == "papír") or (tah_cloveka == "papír" and tah_pocitace == "kámen"):
        print("Vyhrál jsi!\n")
    elif (tah_pocitace == "kámen" and tah_cloveka == "nůžky") or (tah_pocitace == "nůžky" and tah_cloveka == "papír") or (tah_pocitace == "papír" and tah_cloveka == "kámen"):
        print("Prohrál jsi!\n")
    elif tah_cloveka == "konec":
        quit()
    else:
        print("Nerozumím tvému tahu - zkus to znovu a použij diakritiku\n")
