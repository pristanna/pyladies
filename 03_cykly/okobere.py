from random import randrange

skore = 0

while True:
    if skore < 21:
        odpoved = input("Chces pokracovat? ano/ne\n")
        if odpoved == "ano":
            karta=(randrange(2, 10))
            skore=(skore + karta)
            print("Tve skore je: ", skore)
        if odpoved == "ne":
            print("OK, koncime. Tve skore je: ", skore, " bodu.")
            break
    if skore > 21:
        print("Prohral jsi!")
        break
