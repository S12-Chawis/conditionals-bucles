'''Ejercicio 4: Contador regresivo Crea un programa que pida un número positivo al usuario y haga una cuenta regresiva desde ese número hasta 0 usando un bucle while. '''

while True:
    try:
        contador = int(input('Ingresa un numero entero positivo unicamente:'))
        if contador > 0:
            break
        print('El numero debe ser positivo')
    except Exception as e:
        print('Error', e)
        
while contador != -1:
    print(f'Cuenta regresiva! {contador}')
    contador -= 1