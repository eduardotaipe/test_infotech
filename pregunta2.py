# Pregunta 2:
# Escribir un codigo en python que sume y multiplique respectivamente todos los numeros de una lista,
# ejemplo;
# Numeros=1 2 3 4, suma 10, multiplicacion 24.

from random import randint



numbers = [randint(1, 5) for i in range(randint(4,8))]

prod = 1
for i in numbers:
    prod *= i

sum_numbers = sum(numbers)
prod_numbers = prod

if __name__ == "__main__":
    print(f'List numbers: {numbers}')
    print(f'Sum: {sum_numbers}')
    print(f'Multiplication: {prod_numbers}')

