"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""
try:
    MATRIX = []
    N = 0
    while N < 5:
        LIST = []
        i = 0
        SUMM = 0
        print(f"{N + 1}-я строка: ")
        while i < 4:
            ELEMENTS = int(input())
            LIST.append(ELEMENTS)
            i += 1
            SUMM += ELEMENTS
        LIST.append(int(SUMM))
        MATRIX.append(LIST)
        N += 1

    for k, j in enumerate(MATRIX):
        print(MATRIX[k])
except ValueError:
    print("Введите корректное значение")
