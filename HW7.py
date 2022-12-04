import random
import math
print('№1')
my_file = open('Числа.txt', 'w')
N = int(input('Количество записываемых чисел: '))
for i in range(N):
    x = random.randint(1000, 9999)
    my_file.write(str(x) + str('\n'))
my_file.close()
###################################################
print('№2')
my_file = open('Таблица значений.txt', 'w')
a = float(input('Левая граница: '))
b = float(input('Правая граница: '))
h = float(input('Задайте величину шага: '))
while a <= b:
    y = round((a * math.log(1 + (math.sin(math.radians(a)) / a))) /
              a + (math.sin(math.radians(a))), 3)
    my_file.write('При x = ' + str(a) + '; y = ' + str(y) + str('\n'))
    a = round(a + h, 3)
my_file.close()
###################################################
print('№3')
my_file = open('Набор слов.txt', 'r', encoding='utf-8')
c = my_file.readlines()
a = random.choice(c)
b = random.choice(c)
if a != b:
    print('I recieve', a)
    print('You receive', b)
else:
    print('Слова повторяются')
my_file.close()
