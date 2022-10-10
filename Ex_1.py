# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import math


def accuracy_check(input_accuracy):
    if input_accuracy[0] == "0" and input_accuracy[1] == "." and input_accuracy[-1] == "1":
        for i in input_accuracy[2:-2]:
            if i != "0":
                return False
    else:
        return False
    return True


d = ""
check = False
while not check:
    d = input("Введите желаемую точность (0.1 - 0.0000000001): ")
    check = accuracy_check(d)
else:
    accuracy = len(d) - 2

print(round(math.pi, accuracy))
