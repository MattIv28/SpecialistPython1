# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random
numbers = []
sum_dig = 0
n = int(input("Введите число элементов списка: "))

i = 0
while i < n:
    x = random.randint(-100, 100)
    numbers.insert(i, x)
    i += 1
print(numbers)
for digit in numbers:
    if digit > 0 and digit % 2 == 0:
        sum_dig = sum_dig + digit
print(sum_dig)
