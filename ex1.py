from sympy import Limit, Symbol, S 

matricula = 225
c = matricula%10
x = Symbol('x')

def function(x, c):
    return (1 + ((c + 4)/x**3))**x**3

res1 = Limit(function(x,c),x,0).doit() 
res2 = Limit(function(x,c),x,S.Infinity).doit()
res3 = Limit(function(x,c),x,-S.Infinity).doit()

print('O limite para x-->0 é de {}'.format(res1))  #resultado 1
print('O limite para x-->+oo é de {}'.format(res2)) #resultado exp(9)
print('O limite para x-->-oo é de {}'.format(res3)) #resultado exp(9)