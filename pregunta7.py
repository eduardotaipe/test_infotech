# Pregunta 7:
# Desarrollar una funcion que me devuelva el n-esimo fibonacci
# Recordar que la serie fibonacci inicia en uno, es decir que fibonacci(1) = 1, ademas que
# el fibonacci(3) = fibonacci(2) + fibonacci(1)
# Nota: Implementarlo de modo iterativo.


def fibonacci(n):
    if n < 1:
        raise ValueError('You must enter a positive integer greater than zero')

    if n in [1, 2]:
        return 1
    
    a, b = 0, 1
    for i in range(n):
        a, b = b, b + a
    return a


if __name__ == "__main__":
    
    try:
        input_position = int(input('Enter the fibonacci number you want: '))
    except ValueError:
        raise ValueError('You must enter a positive integer.')

    value_fibonnacci = fibonacci(input_position)
    print(f'The fibonacci value at position {input_position} is: {value_fibonnacci}')