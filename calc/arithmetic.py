
from decimal import *
getcontext().prec = 4

def sum(a,b):

    return float(Decimal(a) + Decimal(b))

def difference(a,b):
    return  float(Decimal(a) - Decimal(b))

def product(a,b):
    return float(Decimal(a) * Decimal(b))

def quotient(a,b):
    return float(Decimal(a) / Decimal(b)) 


