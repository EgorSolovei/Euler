"""Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов
будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона."""

num = [1, 2]
for i in range(2, 50):
    num.append(num[i - 2] + num[i - 1])

sum = 0
for i in range(len(num)):
    if num[i] % 2 == 0 and num[i] <= 4_000_000:
        sum += num[i]
print(sum)
