# Pregunta 5:
# Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

from random import randint


def sum_numbers(numbers_list):
    res = sum(numbers_list)
    return res

def multip_numbers(numbers_list):
    res = 1
    for i in numbers_list:
        res *= i
    return res


if __name__ == "__main__":
    
    numbers = [randint(1, 20) for i in range(randint(5,10))]

    sum_total = sum_numbers(numbers)
    prod_total = multip_numbers(numbers)

    print(f'List numbers: {numbers}')
    print(f'Sum: {sum_total}')
    print(f'Multiplication: {prod_total}')

