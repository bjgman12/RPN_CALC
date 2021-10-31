from calc.calc_logic import *

def test_sum_int():
    actual = sum(5,2)
    expected = 7.000

    assert actual == expected

def test_sum_float():
    actual = sum(5.4, 2.1)
    expected = 7.500

    assert actual == expected

def test_difference_int():
    actual = difference(4,3)
    expected = 1.000

    assert actual == expected

def test_difference_neg_float():
    actual = difference(4.0,5.2)
    expected = -1.200

    assert actual == expected

def test_product_neg_float():
    actual = product(2.3,-4.5)
    expected = -10.35
    assert actual == expected 

def test_quotient_float():
    actual = quotient(3,11)
    expected = 0.2727

    assert actual == expected 