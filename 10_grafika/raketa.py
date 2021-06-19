import pyglet
from math import sin

window = pyglet.window.Window(width=1000, height=700)

# nacist raketu
raketa_off = pyglet.image.load("obrazky/raketa_off.png")
raketa_on = pyglet.image.load("obrazky/raketa_on.png")

raketa = pyglet.sprite.Sprite(raketa_off)
raketa.x = window.width / 2 - 30                        # 30 je cca poloviny sirky obrazku

# funkce spoustejici 60x za sekundu funkci let / v podstate slouzi k tomu, abychom mohli odlozit start rakety aby stihla nazhavit motory....
def odstartuj(t):
    pyglet.clock.schedule_interval(let, 1/60) # funkce spoustejici se 60x za sekundu

# nastavit funkci vykrelujici raketu
def let(t):
    if raketa.y < window.height:    # kontrola, jeslti nahodou neni vys nez je vyska okna... a pak ji vratime dolu
        raketa.y += 3               # menit y pozici rakety tak aby se postupne posouvala nahoru
    else:
        raketa.y = -100
    raketa.rotation = sin(raketa.y / 4)

# funkce prepinajici obrazek rakety s plamenem a obrazek rakety bez plamenem
# prepinaji se mezi sebou, ale kod jede normalne dal... jede jakoby ve vedlejsi smycce
def horeni_zapni(t):
    raketa.image = raketa_on
    pyglet.clock.schedule_once(horeni_vypni, 1/100)

def horeni_vypni(t):
    raketa.image = raketa_off
    pyglet.clock.schedule_once(horeni_zapni, 1/100)

# hlavni vykreslovaci funkce
def vykresli():
        window.clear() # toto vycisti okno - v pripade ze v nem neco je
        raketa.draw()

# spust casovac
pyglet.clock.schedule_once(horeni_zapni, 1)
pyglet.clock.schedule_once(odstartuj, 1.5) # funkce ktera nam zpozdi start o 1.5s - tedy dava cas rakete nastartovat motory

# hlavni spusteni
window.push_handlers(on_draw=vykresli)
pyglet.app.run()
