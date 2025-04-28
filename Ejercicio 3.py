'''Bucles Ejercicio 3: Tabla de multiplicar Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10) usando un bucle for.'''

while True:
    try:
        num = int(input('De que numero quieres ver la tabla de multiplicar? (Del 1 al 10):'))
        if num >= 0 and num <= 10:
            break
        print('Recuerda, solo numeros del 1 al 10')
    except Exception as e:
        print('Error', e)
        
for i in range(0, 11):
    result = num * i
    print(f'{num} x {i} = {result}')