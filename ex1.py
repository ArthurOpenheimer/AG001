from sympy import Limit, Symbol, S 

c = 225%10
x = Symbol('x')

def function(x):
    return (1 + ((c + 4)/x**3))**(x**3)

res1 = Limit(function(x), x, 0).doit()
res2 = Limit(function(x), x, S.Infinity).doit()
res3 = Limit(function(x), x, -S.Infinity).doit()

print('O limite para x-->0 é de {}'.format(res1))
print('O limite para x-->+oo é de {}'.format(res2))
print('O limite para x-->-oo é de {}'.format(res3))