# Rozsirena verze tridy Kotatko. Metoda zamnokej() nyni prima parametr zprava.
# Pri kazdem zavolani metody se predava, co presne ma kotatko zamnoukat.


class Kotatko:
    def zamnoukej(self, zprava):
        print('Kotatko: {}'.format(zprava))
        # Toto je skvely priklad trid. Retezec je trida. Retezec ma take metody.... jedna z nich je .format


kotatko = Kotatko()                 # Tady definuju/tvorim novou instanci tridy Kotatko

# Pristup k jendotlivym instancim

kotatko.zamnoukej('Mnau?')
kotatko.zamnoukej('MNAAAAAAAAAU!')

jine_kotatko = Kotatko()
