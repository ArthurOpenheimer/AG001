from sympy import Symbol, solve, tan

c = 225 % 10

def eq1(x):
    return (2**x) + (2 ** (4*x)) - 1 - c

def eq2(w):
    return 5*(w**(1/2)) - (4 * (w**2)) + (w/2) - c

def eq3(a):
    return ((3 * tan((c - 3) * a)) + 2) ** 2

x = Symbol('x')
y = eq1(x)
result1 = solve(y)

w = Symbol('w')
z = eq2(w)
result2 = solve(z)

a = Symbol('a')
b = eq3(a)
result3 = solve(b)

print('Resultado Equação 1: ', result1)
print('Resultado Equação 2: ', result2)
print('Resultado Equação 3: ', result3)