"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

A = [33, 11, 11, 22, 33, 22, 33, 11]
RESULT = max(A, key=lambda x: A.count(x))
print(f"В массиве {A} чаще всего встречается: {RESULT}")
