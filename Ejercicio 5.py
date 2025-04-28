'''Ejercicio Combinado Ejercicio 5: Adivina el número Crea un programa que genere un número aleatorio entre 1 y 10, y le pida al usuario que lo adivine. El programa debe indicar si el número ingresado es mayor, menor o correcto. El usuario tiene hasta 3 intentos.'''

import random as ran   #Se importa la libreria random para sacar un numero aleatorio con el metodo randint

num = ran.randint(1,10)    #Se genera un numero entero aleatorio de 1 a 10

intentos = 3
while intentos > 0:  #Se hace un bucle infinito, que se detiene cuando el contador llegue a 0
    intentos -= 1    #Se resta 1 al contador por cada repeticion
    while True:   #Se pregunta el numero para que adivine
        try:
            guess = int(input('Adivina el numero entero del 1 al 10: '))
            if guess >= 0 and guess <= 10:  #Si esta dentro del rango, se sale del bucle
                break
            print('Recuerda, unicamente de uno a diez')
        except Exception as e:
            print('Error', e)
    if guess < num:      #Verifica si es mayor, menor o igual
        print(f'El numero ingresado ({guess}) es menor')
        print(f'Numero de intentos disponibles: {intentos}')
    elif guess > num:
        print(f'El numero ingresado ({guess}) es mayor')
        print(f'Numero de intentos disponibles: {intentos}')
    else:
        print(f'Enorabuena! has adivinado el numero {num}')
        intentos = 3
        break   #Si adivina el numero, se sale del bucle sin importar que el contador no halla llegado a 0