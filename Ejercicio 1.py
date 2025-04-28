'''Ejercicio 1: Clasificador de números Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.'''

while True:
    try:
        num = int(input('Ingresa un numero entero unicamente:'))
        break
    except Exception as e:
        print('Error', e)
        
if num < 0:
    print(f'El numero {num} es negativo')
elif num > 0:
    print(f'El numero {num} es positivo')
else:
    print(f'El numero {num} es cero')