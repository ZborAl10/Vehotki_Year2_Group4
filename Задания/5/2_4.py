from sympy import *
var('n')
p = product(1-1/(n**2),(n,2,oo))
print(p)
