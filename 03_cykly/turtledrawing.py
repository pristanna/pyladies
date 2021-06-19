from turtle import forward, left, right, exitonclick, penup, pendown
from math import sqrt

#todraw=input("Zadej, co chces nakreslit z tohoto seznamu: kyticka, trojuhelnik, domecek, vesnice, nuhelnik, spirala, 4spirala, 8spirala: ")
todraw = "kyticka"
if todraw == "kyticka":

    penup()
    left(90)
    forward(200)
    pendown()
    '''for cislo in range(18): #zacatek kyticky
        for cislo in range(4):
            forward(50)
            left(90)
        left(20) #konec kyticky
'''
    left(180)
    forward(100) # cast stonku

# prvni strana listku
    length=11
    spacing=30 # o kolik se prodluzuji
    for i in range(6):
        forward(spacing)
        left(90)
        step = 0 # spodni strana listku
        for i in range(20):
            step = (step + 0.5)
            forward(step)
            left(2)
        left(140)
        step = 0 # vrchni strana listku
        for i in range(20):
            step = (step + 0.5)
            forward(step)
            left(2)
        left(50) # srovnej si pozici na listku
        spacing=(spacing * 1.07)

        '''forward(length)
        right(180)
        forward(length)
        left(65)
        forward(spacing)
        length = (length + spacing * 0.4)
        '''
    # spodni cast stonku a obrat na cestu zpet
    forward(30)
    left(180)

# druha strana listku
    length=11
    spacing=30 # o kolik se prodluzuji
    for i in range(6):
        forward(spacing)
        left(90)
        step = 0 # spodni strana listku
        for i in range(20):
            step = (step - 0.5)
            forward(step)
            left(2)
        left(140)
        step = 0 # vrchni strana listku
        for i in range(20):
            step = (step - 0.5)
            forward(step)
            left(2)
        left(50) # srovnej si pozici na listku
        spacing=(spacing * 1.07)

    exitonclick() # Necessary to leave the window open

elif todraw == "trojuhelnik":

    forward(50)
    left(120)
    forward(50)
    left(120)
    forward(50)

    exitonclick() # Necessary to leave the window open

elif todraw == "domecek":

    for cislo in range(4):
        forward(50)
        left(90)
    for i in range(4):
        left(45)
        forward(2 * 50 ** 2)
    for i in range(2):
        left(90)
        forward(50)

    exitonclick() # Necessary to leave the window open

elif todraw == "nuhelnik":

    n = int(input("Kolika nuhelnik chces nakreslit? Zadej n: "))
    a = 200 / n  # delka strany
    vnitrni_uhel = 180 * (1 - 2 / n)
    uhel = 180 - vnitrni_uhel

    for x in range(n):
        forward(a)
        left(uhel)

    exitonclick()

elif todraw == "4spirala":

    step = 0
    left(90)
    for i in range(19):
        step = (step + 3)
        forward(step)
        left(90)
    exitonclick()

elif todraw == "8spirala":

        step = 0
        left(90)
        for i in range(50):
            step = (step + 1)
            forward(step)
            left(45)
        exitonclick()

elif todraw == "spirala":

        step = 0
        left(90)
        for i in range(1000):
            step = (step + 0.1)
            forward(step)
            left(20)
        exitonclick()
