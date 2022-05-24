from sympy import *

x = Symbol('x')
p = Symbol('p')
integ = integrate(x**p, x)
print(integ)
pprint(integ)
