from sympy import Integral, Symbol, S

c = 225 % 10

def f(x):
    return x**3 - (4*(x**2)) + 5*x - c

x = Symbol('x')

area = Integral(f(x), (x, 0, 5)).doit()

print('area = ', area)