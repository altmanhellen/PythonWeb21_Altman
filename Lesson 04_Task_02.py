'''
Задача 2
Даны два целых числа a, b. (a < b). Вывести в порядке убывания все целые числа,
расположенные между a и b (не включая числа a и b), а также количество этих чисел.
В первой строке содержатся два целых числа : a, b. ( 1 <= a, b <= 100).
В первой строке вывести количество чисел в интервале (a, b), во второй строке - числа в порядке убывания.

'''

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = 0

for i in range(b - 1, a, -1):
    x += 1
    print(i, end = " ")

print('\n',x)