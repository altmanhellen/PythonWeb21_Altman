'''
Число десятков

Дано целое неотрицательное число N, определите число десятков в нем (предпоследнюю цифру числа).
Если предпоследней цифры нет, то можно считать, что число десятков равно нулю.

Формат входных данных
На вход дается целое положительное число N (0 ≤ N ≤ 1000000).

Формат выходных данных
Выведите одно целое число - ответ на задачу.

'''

number = int(input('Enter number: '))

print((number // 10) % 10)