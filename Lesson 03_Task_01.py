'''
Задача 1

Нечетные цифры

В первой строке содержится целое число N (1 < N < 10 ^ 9). С помощью операций деления нацело
и взятия остатка от деления определить, имеются ли в записи числа N нечетные цифры.
Если имеются, то вывести "True", если нет – вывести "False"

'''

a = [int(input('Введите целое число N (1 < N < 10 ^ 9): '))]

for n in a:
    if (n % 10) % 2 != 0:
        print('True')
    elif (n // 10) % 10 % 2 != 0:
        print('True')
    elif (n // 100) % 10 % 2 != 0:
        print('True')
    elif (n // 1000) % 10 % 2 != 0:
        print('True')
    elif (n // 10000) % 10 % 2 != 0:
        print('True')
    elif (n // 100000) % 10 % 2 != 0:
        print('True')
    elif (n // 1000000) % 10 % 2 != 0:
        print('True')
    elif (n // 10000000) % 10 % 2 != 0:
        print('True')
    elif (n // 100000000) % 10 % 2 != 0:
        print('True')
    elif (n // 1000000000) % 10 % 2 != 0:
        print('True')
    else:
        print('False')