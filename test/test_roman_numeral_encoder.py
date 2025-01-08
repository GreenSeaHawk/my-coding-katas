from src.roman_numeral_encoder import roman_numeral_encoder

def test_works_for_1():
    assert roman_numeral_encoder(1) == 'I'

def test_works_for_2():
    assert roman_numeral_encoder(2) == 'II'

def test_works_for_4():
    assert roman_numeral_encoder(4) == 'IV'

def test_works_for_5():
    assert roman_numeral_encoder(5) == 'V'

def test_works_for_10():
    assert roman_numeral_encoder(10) == 'X'

def test_works_for_12():
    assert roman_numeral_encoder(12) == 'XII'

def test_works_for_60():
    assert roman_numeral_encoder(60) == 'LX'

def test_works_for_75():
    assert roman_numeral_encoder(75) == 'LXXV'

def test_works_for_91():
    assert roman_numeral_encoder(91) == 'XCI'