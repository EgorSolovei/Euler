"""Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5."""

n = 1000
sum = 0
delt = []
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        delt.append(i)
print(sum)
print(delt)

print('Bucnwiuiw')
print('Hey Git')