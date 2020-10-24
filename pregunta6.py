# Pregunta 6:
# Crear una funcion que determine si dado una serie de parentesis, estas se encuentran en pares, es
# decir,
# abierto '(' y cerrado ')'.
# Ejm:
#  Entrada: '(()()())()()(())'
#  Salida: True
#  Entrada: '(()('
#  Salida: False


def parenthesis_pair(data):
    count_open = 0
    count_close = 0
    if data:
        for i in data:
            if count_close > count_open:
                return False
            if i == '(':
                count_open += 1
            elif i == ')':
                count_close += 1
            else:
                raise ValueError("Just enter '(' or ')'.")
        
        if count_open == count_close:
            return True
        return False
    raise ValueError("You must enter '(' or ')'.")

if __name__ == "__main__":
    parenthesis = input("Enter only '(' or ')': ")
    pairs = parenthesis_pair(parenthesis)
    
    print(f'Output: {pairs}')

