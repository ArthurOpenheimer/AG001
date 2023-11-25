from sympy import symbols, Eq, solve

c = 225 % 10

I1, I2, I3 = symbols('I1 I2 I3')

V1 = (c + 2) * 4
V2 = (c + 1) * 5

R1, R2, R3 = 12, 4, 6

eq1 = Eq(I1, I2 + I3)
eq2 = Eq(V1, I1*R1 + I3*R3)
eq3 = Eq(V2, I2*R2 - I3*R3)

results = solve((eq1, eq2, eq3), (I1, I2, I3))

print('I1 = ', results[I1])
print('I2 = ', results[I2])
print('I3 = ', results[I3])