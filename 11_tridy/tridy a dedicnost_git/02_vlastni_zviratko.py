class Zvire:
    def __init__(self, jmeno, druh, majitel, oblibene_jidlo, vaha):
        print('Vytvarim zvire jmenem: {}'.format(jmeno))
        self.jmeno = jmeno
        self.druh = druh
        self.majitel = majitel
        self.oblibene_jidlo = oblibene_jidlo
        self.vaha = vaha

    def zvuk(self, citoslovce):
        print('Jsem {} a mluvim takto: {}'.format(self.druh, citoslovce))

    def __str__(self):
        #return "Jmenuji se " + self.jmeno + " a jsem " + self.druh + " patrici majiteli " + self.majitel + " chutna mi " + self.oblibene_jidlo + " a vazim " + str(self.vaha) + " kg"
        return "Jmenuji se {} a jsem {} patrici {}. Chutna mi {} a vazim {} kg" .format(self.jmeno, self.druh, self.majitel, self.oblibene_jidlo, self.vaha) # obe varianty jsou mozne ale jen ta prvni se provede

zvire1 = Zvire('Pamfrnak','hroch', 'anca', 'ryba', 1000 )


print(zvire1)
zvire1.zvuk('Buuuuf')
