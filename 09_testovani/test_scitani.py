
import pytest
from scitani import secti, deleni

def test_secti():
    assert secti(2, 3) == 5

def test_secti_jinak():
    assert secti(2, 3) == 4, 'pokus' # pokus je hodnota vyjimky

def test_deleni():
    assert deleni(1, 2) == 0.5

# Testovani i toho ze to nefunguje
# vyhodi vyjimku ze to nevyhodilo vyjimku

def test_deleni_nulou():
    with pytest.raises(ZeroDivisionError):
        deleni(1, 0)
