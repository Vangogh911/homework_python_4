# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
#
# Пример:
# k=2 -> 2x**2 + 4x + 5 = 0 или x**2 + 5 = 0 или 10x**2 = 0
# k=5 -> 3x**5 + 5x**4 - 6x**3 - 3x = 0
import random


def make_numbers_list():
    k = int(input("Введите значение степени: "))
    line = []
    while k > 0:
        num = random.randint(0, 100)
        if num == 0:
            k -= 1
            continue
        else:
            if k > 1:
                line.append(f"{num}x**{k}")
                k -= 1
            else:
                line.append(f"{num}x")
                k -= 1
    return line


def make_numbers_string(line):
    string_line = ""
    for i in range(len(line) - 1):
        sign = random.randint(0, 1)
        if sign == 0:
            string_line += line[i] + " + "
        else:
            string_line += line[i] + " - "
    string_line += line[-1] + " = 0"
    return string_line


text_list = make_numbers_list()
text_line = make_numbers_string(text_list)
with open("text.txt", "w") as f:
    f.write(text_line)
f.close()
print("Файл готов")
