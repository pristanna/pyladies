from math import pi

def obsah_elipsy(a, b):
    return pi * a * b

def objem_eliptickeho_valce(a, b, v):
    return obsah_elipsy(a, b) * v

strana_a = int(input("Zadej stranu a:"))

print(obsah_elipsy(20, 30))
print(objem_eliptickeho_valce(20, 30, 10))


# print(pi * a * b) # Print lze pouzit, ale jen vypise a nemuzu to pak uz nikde dal pouzit
