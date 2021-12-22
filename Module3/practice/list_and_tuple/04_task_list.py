# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here

my_list = [10, 5, 7, 2, -1, 8, -3, 9]
sum_dig = 0
for digit in my_list:
    if digit > 0:
        sum_dig = sum_dig + digit
print(sum_dig)
