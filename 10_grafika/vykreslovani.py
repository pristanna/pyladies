import pyglet
window = pyglet.window.Window(width=1000, height=700)

# obrazek nacten do promenne
obrazek = pyglet.image.load("obrazky/had.png")

# obrazek musime nacist v pygletu
# f-ce vytvori tridu....
# Sprite - je trida - tridy se pisou s velkym pismenem dle norem PEP8
# Auto PEP8 script - sam nam kod znormalizuje

had = pyglet.sprite.Sprite(obrazek)
had.x = window.width / 2 - 50 # umistuje levy horni roh obrazku, tzn. 50 urcuje sirku poloviny obrazku
had.y = window.height / 2 - 50
had.rotation = 30

# kdyz vyjedu s prvkem v okne mimo obrazovku, tak mi prvek zmizi... pyglet si ho nepamatuje

def vykresli():
        window.clear() # toto vycisti okno - v pripade ze v nem neco je
        had.draw()

# defaultne se obrazky vykresluji vlevo dole - jakoby x = 0 a y = 0
# v jinych knihovnach to muze byt napriklad vlevo nahore

window.push_handlers(on_draw=vykresli)

pyglet.app.run()
