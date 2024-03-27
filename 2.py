"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
Начиная с 1 и 2, первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""
x = 4_000_000

# Вариант 1
result = 0
first_element = 0
two_element = 1
while True:
    first_element, two_element = two_element, two_element + first_element
    if first_element % 2 != 0:
        continue
    if first_element > x:
        break
    result += first_element
print(result)
