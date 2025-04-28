'''Ejercicio Combinado Ejercicio 5: Adivina el número Crea un programa que genere un número aleatorio entre 1 y 10, y le pida al usuario que lo adivine. El programa debe indicar si el número ingresado es mayor, menor o correcto. El usuario tiene hasta 3 intentos.'''

import random

num = random.randint(1,10)

intentos = 3
while intentos > 0:
    intentos -= 1
    while True:
        try:
            guess = int(input('Adivina el numero entero del 1 al 10: '))
            if guess >= 0 and guess <= 10:
                break
            print('Recuerda, unicamente de uno a diez')
        except Exception as e:
            print('Error', e)
    if guess < num:
        print(f'El numero ingresado ({guess}) es menor')
        print(f'Numero de intentos disponibles: {intentos}')
    elif guess > num:
        print(f'El numero ingresado ({guess}) es mayor')
        print(f'Numero de intentos disponibles: {intentos}')
    else:
        print(f'Enorabuena! has adivinado el numero {num}')
        intentos = 4
        break