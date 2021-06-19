# rozpohybovat mic tak, aby letel stejne jako raketa
# odrazil se od spodni hranice a zase letel nahoru
# kdyz leti nahoru, tak se rychlost pomalu zpomaluje. kdyz dosahne rychlosti 0 a leti dolu, tak se zase zacne pomalu zrychlovat
# pridat odrazeni od zeme
# micek posleme i po ose x do strany tak aby se odrazel pod uhlem... v podstate se to da udelat jen zmenou smeru

import pyglet
from math import sin

window = pyglet.window.Window(width=1000, height=700)

# nacist micek
micek = pyglet.image.load("obrazky/micek.png")
objekty = []
objekty.append({'objekt': pyglet.sprite.Sprite(micek), 'smer': 4})

# smer si zapisu do slovniku jako dalsi klic

def pohyb(t):
    objekty[0]['objekt'].y += objekty[0]['smer']
    if objekty[0]['objekt'].y > window.height:
        objekty[0]['objekt'] = - objekty[0]['smer']

# hlavni vykreslovaci funkce
def vykresli():
        window.clear() # toto vycisti okno - v pripade ze v nem neco je
        objekty[0]['objekt'].draw()

# hlavni spusteni
pyglet.clock.schedule_interval(pohyb, 1/60) # funkce spoustejici se 60x za sekundu
window.push_handlers(on_draw=vykresli)
pyglet.app.run()
