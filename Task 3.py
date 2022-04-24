"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
Самый большой делитель - это корень из самого числа
"""

num = [1] # Список простых чисел
for i in range(1, 20, 2):
    for j in range(2, i):
        if i % j != 0 and i not in num:
            num.append(i)
print(num)
print(5 / 5)

# решение из интернета
num = 600851475143
d = 2
while num != 1 and d*d <= num:
    if num % d == 0:
        num //= d
    else:
        d += 1
print(num)
print('LALAL')