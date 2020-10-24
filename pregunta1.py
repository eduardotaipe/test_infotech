# Pregunta 1:
# Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma: los 5 mas bajos
# y los 5 mas altos

from random import randint


numbers = [randint(1, 100) for i in range(10)]

sorted_numbers = sorted(numbers)
mid = len(numbers) // 2

low_numbers = sorted_numbers[:mid]
high_numbers = sorted_numbers[mid:]

if __name__ == "__main__":
    print(f'Random list numbers: {numbers}')
    print(f'Ordered list numbers: {sorted_numbers}')

    print(f'Sum of the 5 first numbers: {sum(low_numbers)}')
    print(f'Sum of the 5 last numbers: {sum(high_numbers)}')
