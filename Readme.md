RESOLUCION DE TEST INFOTECH

***Para la pregunta 4 es necesario realizar algunos pasos descritos mas adelante.***


Pregunta 1:
    Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma: los 5 mas bajos
    y los 5 mas altos

Pregunta 2:
    Escribir un codigo en python que sume y multiplique respectivamente todos los numeros de una lista,
    ejemplo;
        Numeros=1 2 3 4, suma 10, multiplicacion 24.

Pregunta 3:
    Que es INDEX (indice) en base de datos, indicar beneficios y desventajas

Pregunta 4:
    Hacer un API REST que tenga la funcion de listar las carpetas y archivos y ordenar por tamaño o
    fecha

    NOTA:
        1. Crear un entorno virtual e ingresar en el e instalar los requerimientos estando en la carpeta pregunta4:
            comando:
                python -m venv env
                source env/Scripts/activate
                pip install -r requirements.txt
        
        2. Ejecute el archivo app.py
            comando:
                python app.py
        3. Use postman u otra herramienta para testing de APIS
        4. La aplicación se ejecuta en:
            http://localhost:5000/api
            o
            http://127.0.0.1:5500/api
        5. Los campos son:
            dato principal:
                        key = path              value = ruta_de_directorio
            ordenamiento:
                        key = order             por tamaño =>   value = file_size
                                                por fecha  =>   value = file_create_date
            
            ordenamiento en reversa:
                        key = reverse_order     value = True
                        
                        - por defecto esta en False



Pregunta 5:
    Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos
    los números de una lista.
    Por ejemplo:
        sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

Pregunta 6:
    Crear una funcion que determine si dado una serie de parentesis, estas se encuentran en pares, es
    decir, abierto '(' y cerrado ')'.
    Ejm:
        Entrada: '(()()())()()(())'
        Salida: True
        Entrada: '(()('
        Salida: False

Pregunta 7:
    Desarrollar una funcion que me devuelva el n-esimo fibonacci
    Recordar que la serie fibonacci inicia en uno, es decir que fibonacci(1) = 1, ademas que
    el fibonacci(3) = fibonacci(2) + fibonacci(1)
    Nota: Implementarlo de modo iterativo.