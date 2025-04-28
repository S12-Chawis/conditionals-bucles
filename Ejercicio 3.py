'''Bucles Ejercicio 3: Tabla de multiplicar Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10) usando un bucle for.'''

while True:    #Se pide el numero del 1 al 10
    try:
        num = int(input('De que numero quieres ver la tabla de multiplicar? (Del 1 al 10):'))
        if num >= 0 and num <= 10:    #Si cumple el rango se sale del bucle
            break
        print('Recuerda, solo numeros del 1 al 10')
    except Exception as e:
        print('Error', e)
        
for i in range(1, 11):      #Se itera 10 veces para miltiplicar este numero con su sucesivo desde el 1 hasta el 10
    result = num * i
    print(f'{num} x {i} = {result}')