#############################################
print('№1')
a = int(input('Введите число: '))
for i in range(1, 11):
    print(a, 'x', i, '=', a * i)
#############################################
print('№2')
N = int(input('Количество чисел: '))
summ = 0
for i in range(N):
    b = float(input('Введите число: '))
    summ = summ + b
print('Сумма чисел:', summ)
#############################################
print('№3')
a = input('Введите строку: ')
while a != 'PRINT':
    print('id', a, sep='')
    a = input()
#############################################
print('№4')
print('Введите два числа: ')
a = float(input())
b = float(input())
while b != 0:
    print(a + b, a - b, a * b, round(a / b, 3), sep='\n')
    print('Введите два числа: ')
    a = float(input())
    b = float(input())
else:
    print('На ноль делить нельзя!')
