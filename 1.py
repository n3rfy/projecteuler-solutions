"""
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""
x = 1000

# Вариант 1.
result = 0
for element in range(1, x):
    if element % 3 != 0 and element % 5 != 0:
        continue
    result += element
print(result)


# Вариант 2.
def arithmetic_progression_sum(first: int, last: int, n: int):
    return (first + last) * n / 2


count_tree = (x - 1) // 3
tree_sum = arithmetic_progression_sum(3, 3 * count_tree, count_tree)
count_five = (x - 1) // 5
five_sum = arithmetic_progression_sum(5, 5 * count_five, 999 // count_five)
count_fifteen = (x - 1) // 15
fifteen_sum = arithmetic_progression_sum(15, 15 * count_fifteen, count_fifteen)
result = tree_sum + five_sum - fifteen_sum
print(result)
