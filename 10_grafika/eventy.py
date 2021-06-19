import pyglet
window = pyglet.window.Window()

# tato funkce nam posle vypise klavesu, kterou uzivatel stisknul
# tato funcke musi mit parametr, protoze handler ji prijimia - a to i v pripade, ze ji nakonec nepouzije
def zpracuj_text(text):
    print("Stisknuto:", text)

# Odchytavani udalosti
# on_text spust9 funcki s nazvem zpracuj_text
window.push_handlers(on_text=zpracuj_text)

pyglet.app.run()
