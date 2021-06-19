barva_travy = 'zelena'

def secti(a, b):
    return a + b

print('v louka.py')

# Toto ej nebezpecne.... protoze
# vse by melo byt ve funkcich, ktere se spusti az kdyz je volame.... toto print se totiz vypise samo...
# nemit nic na te nejvycssi urovni
# obzvlast problematicke je, kdyz napriklad ceka na input
# lepe tedy vypsat timto zpusobem:

def vypis():
        print ('v louka.py')
