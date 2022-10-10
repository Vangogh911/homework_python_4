# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Решать через множества и еще каким-нибудь способом кроме множества
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

# Решение 1
# line = "47756688399943"
# uniq_numbers = []
# for i in line:
#     if line.count(i) == 1:
#         uniq_numbers.append(int(i))
# print(uniq_numbers)

# Решение 2
# def number_to_list(line):
#     numbers = []
#     while line > 10:
#         numbers.append(line % 10)
#         line = int(line / 10)
#     else:
#         numbers.append(line)
#     numbers.reverse()
#     return numbers
#
#
# def uniq_numbers(line):
#     numbers = number_to_list(line)
#     uniq_numbers_list = []
#     for i in numbers:
#         if numbers.count(i) == 1:
#             uniq_numbers_list.append(i)
#     return uniq_numbers_list
#
#
# print(uniq_numbers(47756688399943))
# print(uniq_numbers(1113384455229))
# print(uniq_numbers(1115566773322))


# Решение 3 через множества
def number_to_list(line):
    numbers = []
    while line > 10:
        numbers.append(line % 10)
        line = int(line / 10)
    else:
        numbers.append(line)
    numbers.reverse()
    return numbers


def uniq_numbers(numbers):
    numbers_set = set()
    uniq_numbers_list = []
    for i in numbers:
        if i not in numbers_set:
            numbers_set.add(i)
            uniq_numbers_list.append(i)
        else:
            if i in uniq_numbers_list:
                uniq_numbers_list.remove(i)
    return uniq_numbers_list


print(uniq_numbers(number_to_list(47756688399943)))
print(uniq_numbers(number_to_list(1113384455229)))
print(uniq_numbers(number_to_list(1115566773322)))
