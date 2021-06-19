# Napiste program, ktery se zepta na prijmeni uzivatelky/uzivatele a zkus9 podel n2j uhodnout pohlav9

prijmeni = input("Zadejte sve prijmeni:")
prijmeni = prijmeni.lower()

if "ova" in prijmeni or "ová" in prijmeni:
    print("Jste zena")
else:
    print("Jste muz, nejste češka nebo jste zadal nejakou blbost.... :-)")
