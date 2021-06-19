#### N-tice aneb tupples
# možno kombinovat různé datové typy

# N-tici využáváme ve chvíli kdy funkci předáváme nějáké argumenty

def ntice(hodnota, retezec):                # Toto uz je n-ntice
    return True, "Ahoj"

logicka, string = ntice(123, "Ahoj")
print(logicka)
print(string)

promenna = (1, 2, 3, 'Ahoj')
prazdna_ntice = ()
prazdna_ntice = ('Ahoj', )      # I pokud chci ulozit jen jednu hodnotu, musim pouzit carku vcetne mezery

# N tice jsou definovany kulatymy zavorkami
# seznamy jsou definovany hranatymi zavorkami
