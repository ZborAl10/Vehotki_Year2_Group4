from sympy import *
x = symbols('x')
L = Limit((3*x*x+2*x+1)/(2*x*x*x-x),x,0)
l = limit((3*x*x+2*x+1)/(2*x*x*x-x),x,0)
print(L,' = ', l)
ll = limit((3*x*x+2*x+1)/(2*x*x*x-x),x,0,'-')
lr = limit((3*x*x+2*x+1)/(2*x*x*x-x),x,0,'+')
if (ll!=lr):
    print('Предел не существует')
    