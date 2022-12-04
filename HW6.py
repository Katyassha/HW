import random
print('№1')
n = int(input('Задайте размер списка: '))
a = int(input('Задайте начало диапазона: '))
b = int(input('Задайте конец диапазона: '))
s = list()
for i in range(n):
    s.append(random.randint(a, b + 1))
print(s)
print(len(s))
print(max(s))
print(min(s))
s.sort()
print(s)
s.sort(reverse=True)
print(s)
###################################################
print('№2')
n = int(input('Задайте размер списка: '))
s = list()
for i in range(n):
    s.append(random.randint(0, 1))
print(s)
print(s.count(0))
print(s.count(1))
s0 = list()
for i in range(len(s)):
    if s[i] == 0:
        s0.append(i)
print(s0)
###################################################
print('№3')
n = int(input('Задайте размер списка: '))
s = list()
for i in range(n):
    s.append(random.randint(0, 9))
print(s)
x = int(input('Задайте значение, которое нужно удалить из списка: '))
for i in range(len(s)):
    if x in s:
        s.remove(x)
print(s)
