from sympy import *

x, y = symbols('x y', real=True, positive=True)
var = [x, y]

eq1 = tan(x**2 - y) - 0.48*(x + y)
eq2 = (x - 0.2)**2 - 3*y**2 - 1.5
system = [eq1, eq2]

sol = nonlinsolve(system, var)
print(sol)
pprint(sol)
