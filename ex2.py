from sympy import Integral, Derivative, Symbol, cos
from math import pi

c = 225 % 10
x = Symbol('x')

def v(x):
    return 15 * 40 * pi * cos((40 * pi * x) - c)

aceleracao = Derivative(v(x), x).doit()
deslocamento = Integral(v(x), x).doit()

print('Aceleração: ', aceleracao)
print('Deslocamento: ', deslocamento)
print('Aceleração em t = 10: ', aceleracao.subs({x: 10}))

