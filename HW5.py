print('№1')
n = int(input('Колчиество слов: '))
# каждое слово вводится на новой строке
s = ''
for i in range(1, n + 1):
    a = input()
    s += a[0].upper()
print(s)
#########################################
print('№2')
s = input('Введите строку: ')
print(len(s.replace(' ', '')))
print(s[0])
print(s[-1])
a = ''
for i in reversed(s):
    a += i
print(a)
print(s[::2])
print(s[1::2])
#########################################
print('№4')
while True:
    s = input('Введите строку: ')
    if s.upper() != 'STOP':
        if s.isalpha():
            print('Буквенная строка')
        elif s.isdigit():
            print('Цифровая строка')
        elif s.isalnum():
            print('Смешанная строка')
        elif not s.isalnum():
            print('')
    else:
        break
#########################################
print('№3')
while True:
    s = input('Введите строку: ')
    if s.isalpha():
        a = input('Искомый символ: ')
        print(s.upper().count(a.upper()))
    elif s.isdigit():
        for i in range(0, len(s)):
            print(int(s[i]) * 10)
    for i in range(0, len(s)):
        if not s[i].isalnum():
            print(i)
