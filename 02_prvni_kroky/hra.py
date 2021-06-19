# Kamen nuzky papir

import random

moznosti = ["kamen", "nuzky", "papir"]

tah_pocitace = (random.choice(moznosti))

tah_cloveka = input("Jaky je tvuj tah - kamen, nuzky, nebo papir? Zvol: ")

if tah_cloveka == "kamen":
    if tah_pocitace == "kamen":
        print("Remiza")
    if tah_pocitace == "nuzky":
        print("Vyhral jsi!")
    if tah_pocitace == "papir":
        print("Prohral jsi!")
elif tah_cloveka== "nuzky":
    if tah_pocitace == "nuzky":
        print("Remiza")
    if tah_pocitace == "papir":
        print("Vyhral jsi!")
    if tah_pocitace == "kamen":
        print("Prohral jsi!")
elif tah_cloveka== "papir":
    if tah_pocitace == "papir":
        print("Remiza")
    if tah_pocitace == "kamen":
        print("Vyhral jsi!")
    if tah_pocitace == "nuzky":
        print("Prohral jsi!")
else:
    print("Nerozumim tvemu tahu - zkus to znovu")

print("Tah pocitace byl: ", tah_pocitace)
