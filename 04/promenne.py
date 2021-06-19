from math import pi

obsah = 0 # toto je globalni promenna, nevidim na ni mimo tu funkci
a = 30 # toto je globalni promenna, nevidim na ni mimo tu funkci

def obsah_elipsy(a, b): # toto je lokalni promenna
    obsah = pi * a * b # toto je take lokalni promenna
    a = a + 20  # toto zde je naprd, protoze na to po skonceni funkce zapomene
    return pi * a * b

obsah_elipsy(a, b)
print(a) # toto vrati 30 
