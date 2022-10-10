# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_dividers(n):
    divider = 1
    dividers = []
    while divider < n:
        if prime(divider):
            if n % divider == 0:
                dividers.append(divider)
        divider += 1
    return dividers


print(prime_dividers(78351))
