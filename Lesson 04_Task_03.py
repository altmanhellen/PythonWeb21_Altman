'''
Задача 3.
Даны два целых числа a и b. Найти сумму квадратов чисел от a до b включительно.

'''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = 0
s = 0

for i in range(a, b + 1):
    x += 1
    s += i * i

print(s)