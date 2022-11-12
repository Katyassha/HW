import math
import random
#############################################
print('№5')
N = int(input('Введите число: '))
for i in range(1, N + 1):
    if i % 5 != 0:
        print('Длина окружности с радиусом', i, ':', round(2 * math.pi * i, 2))
        print('Площадь окружности с радиусом', i, ':',  round(i**2 * math.pi, 2))
#############################################
print('№4')
while True:
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    if a != 0 and b != 0 and b > a:
        M = random.randint(a, b)
        for i in range(1, M + 1):
            print(round(math.log10(i), 3))
    c = input('Желаете продолжить? Y/N\n')
    if 'Y' in c:
        continue
    else:
        break
#############################################
print('№1')
N = int(input('Введите число: '))
a = int(input('Левая граница: '))
b = int(input('Правая граница: '))
for i in range(1, N + 1):
    if (i % 2 != 0) and i not in range(a + 1, b + 1):
        print(i)
##############################################
print('№2')
while True:
    a = input('Введите команду: ')
    if 'Лого' in a:
        b = input('Введите строку: ')
        print('LN(', len(b), ') = ', round(math.log(len(b)), 2), sep='')
    if 'Триго' in a:
        c = float(input('Введите число: '))
        d = round(math.radians(c), 6)
        print('sin(', c, ') = ', math.sin(d), sep='')
        print('cos(', c, ') = ', math.cos(d), sep='')
        print('tg(', c, ') = ', math.tan(d), sep='')
        print('ctg(', c, ') = ', math.cos(d) // math.sin(d), sep='')
    if 'Конец' in a:
        break
#############################################
print('№3')
while True:
    N = int(input('Введите число до 1000: '))
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    if a <= N <= b or b <= N <= a:
        print('Lucky!')
    else:
        print('Try again!')
