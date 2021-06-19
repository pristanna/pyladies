def obsah_ctverce(a):
    return a * a

def objem_krychle(a, v):
    return obsah_ctverce(a) * v

print(objem_krychle(3, 7))
print("Obsah ctverce je " + str(obsah_ctverce(3))) # obsah_ctverce(3, 8) " a objem kvadru je " objem_krychle(3, 8)) # Tohle nefunguje 3, 8, 7, musi se to prevest na string pomoci str funkce
