# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x**9 - 16x**8 + 3x**7 + 15x**4 - 2x**3 + x**2 + 20 = 0
# 17x**9 + 15x**8 - 8x**7 + 15x**6 - 10x**4 + 7x**3 - 13x + 33 = 0
#
# Результат:
# 40x**9 - x**8 - 5x**7 + 15x**6 +5x**4 + 5x**3 + x**2 - 13x + 53 = 0


def text_to_list(file_name):
    with open(file_name, "r") as f:
        text = f.readline()
    f.close()
    text = text[:-4].split()
    list1 = []
    for i in text:
        list1.append(i.split("x"))
    return list1


def list_to_2d_list(list):
    i = 0
    while i < len(list):
        if list[i][0] == "+" or list[i][0] == "-":
            if list[i + 1][0] == "":
                list[i + 1][0] = f"{list[i][0]}1"
            else:
                list[i + 1][0] = f"{list[i][0]}{list[i + 1][0]}"
            del list[i]
            i -= 1
        i += 1
    return list


def list_2d_to_dict(list):
    dict_num = {}
    for i in list:
        if len(i) > 1:
            dict_num[int(i[1][2:])] = int(i[0])
        else:
            dict_num[0] = int(i[0])
    return dict_num


def dict_to_string(dict1, dict2):
    max_key = max(dict1.keys())
    if max_key < max(dict2.keys()):
        max_key = max(dict2.keys())

    dict3 = {}
    for i in range(max_key + 1):
        if dict1.get(i) is not None and dict2.get(i) is not None:
            dict3[i] = dict1[i] + dict2[i]
        elif dict1.get(i) is not None and dict2.get(i) is None:
            dict3[i] = dict1[i]
        elif dict1.get(i) is None and dict2.get(i) is not None:
            dict3[i] = dict2[i]
        else:
            continue
    string_line = ""
    for i in range(max_key + 1):
        if dict3.get(max_key - i) is not None:
            if max_key - i != max_key:
                if dict3[max_key - i] > 0:
                    string_line += " + "
                else:
                    string_line += " - "
            if abs(dict3[max_key - i]) == 1:
                string_line += f"x**{max_key - i}"
            elif max_key - i == 0:
                string_line += f"{abs(dict3[max_key - i])}"
            elif max_key - i == 1:
                string_line += f"{abs(dict3[max_key - i])}x"
            else:
                string_line += f"{abs(dict3[max_key - i])}x**{max_key - i}"
    string_line += " = 0"
    return string_line


dict1 = list_2d_to_dict(list_to_2d_list(text_to_list("file1.txt")))
dict2 = list_2d_to_dict(list_to_2d_list(text_to_list("file2.txt")))

string_line = dict_to_string(dict1, dict2)
with open("file3.txt", "w") as f:
    text = f.write(string_line)
f.close()
