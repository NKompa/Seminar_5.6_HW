# Программа принимает на вход вещественное число и показывает сумму его цифр: 6782 -> 23; 0,56 -> 11

num = input('Введите число: ')

# for i in ['-', '.', ',']:
#     if i in num:
#         num = num.replace(i, "")
# sum = 0
# for i in num:
#     sum = sum + int(i)
# print(sum)

num_list = list(filter(lambda x: x.isdigit(), list(num)))
num_sum = sum(list(map(int,num_list)))

print(num_sum)