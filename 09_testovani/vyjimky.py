def f():
    print(1)
    1/0
    print(2)

#raise - spustí mechanismus vyhození chyby
#zero DevisionError()
#eg raise ZeroDivisionError() #  tuto chyby jsem si vyrobila sama

def validace(n):
    if n< 0:
        raise Exception('n nema byt zaporne')
    if n>= 20:
        raise Exception('n ma byt mensi nez 20')

validace(5)
validace(-5)


try:
    validace(-5)
except:
    pass


try:
    validace(-5)  # jakmile nastane vyjimka tak to okamzite skoci do bloku except
    print('je to ok')
except:
    print('chyba')

# Hodi se abychom byli schopny zachytit jen urcity typ vyjimky

def nacti():
    i = int(input('>'))
    if i < 0:
        raise ValueErroror('nema to byt zaporne')

try:
    nacti()
except ValueError as e: # e je parametr, do ktereho si potom nactu error
    print('chyba:', e)

def zadani_vstupu():
    try: # osetruje si chybu, zabranuje tomu aby funkce skoncila
        i = nacti()
    except ValueError as e:
        print('chyba Value Error')
    except Exception as e:
        print('chyba', e)
    else:
        print(ok:, i)

zadani_vstupu() # zde si zkuste ruzne
