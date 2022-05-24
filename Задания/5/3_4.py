from sympy import *

x = Symbol('x')
D = diff(x**x, x)
print(D)
pprint(D)
