'''
Задача 1
Напишите программу, которая по заданному натуральному n печатает рисунок (см. ниже).
В первой строке содержится n – количество строк. (1 <= n <= 20). Вывести рисунок.

'''

n = int(input())
a = ['*', '.', '*']
ans = []
i = 1

while i <= n:
    ans = [a[-1] * i + a[-2] * i + a[0] * i]
    i += 1
    print(*ans)