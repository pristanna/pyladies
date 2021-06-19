teplota=input("Zadej teplotu: ")

if teplota < 0:
    print("Už mrzne")
elif teplota == 0:
    print("Je přesně na nule!")
elif teplota > 0 and teplota < 16:
    print("Je pořádná kosa, na kraťasy to ještě není")
elif teplota > 16 and teplota < 30:
    print("Už můžeš vytáhnout kraťasy!")
elif teplota > 30:
    print("Vedro! Vyraž raději někam k vodě!")
else:
    print("Asi něco nefunguje... zkus to znovu")
