# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму: Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input('Введите число: '))
# numbers = {}
# a = 0
# sum = 0
# for i in range(1,n+1):
#     a = (1+1/i)**i
#     numbers[i] = round(a,2)
#     sum +=a
#
# print(f'Последовательность: {numbers}')
# print(f'Сумма чисел последовательности = {round(sum,2)}')

numbers = {i:round((1+1/i)**i,2) for i in range(1,n+1)}
sum_numbers = sum(numbers.values())

print(f'Последовательность: {numbers}')
print(f'Сумма чисел последовательности = {sum_numbers}')