# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here

cow = int(input("Введите количество коров "))

if cow % 10 == 1 and cow != 11:
    print(cow, "корова")
elif 2 <= cow % 10 <= 4 and cow //10 != 1:
    print(cow, "коровы")
else:
    print(cow, "коров")
