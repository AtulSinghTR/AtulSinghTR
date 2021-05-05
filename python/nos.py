print(0.1+0.2)
print(3//2)
print(3/2)

# no=float(input('Enter a base: '))
# ex=float(input('Enter an exponent: '))
# out=str(no ** ex)
# print(f"{no} to the power of {ex} is {out}")

print(round(2.5), round(3.5), round(3.1417), round(3.1417), round(3.1488), round(3.2488), round(3.25))
print(round(3.14159, 3), round(3.14159, 2))
print(abs(-2))
print(pow(-2, 2))
print(pow(3, 3, 2))  # 3^3 % 3

a=2.0
print(a.is_integer())

a=2.5
print(a.is_integer())

no=float(input('Enter a no: '))
print(f'{no} rounded to 3 decimal places is:',str(round(no,3)))
print(f'The absolute value of {no} is',str(abs(no)))

no1=float(input('Enter a no: '))
no2=float(input('Enter another no: '))
out = (no2 - no1).is_integer()
print(f'The difference between {no2} and {no1} is an integer? {out}!') 

out1 = float(3) ** float(0.125)
print(f'{out1:.3f}')

out2=float(150000)
print(f'{out2:,.2f}')

out3=float(2/10)
print(f'{out3:,.2%}')




