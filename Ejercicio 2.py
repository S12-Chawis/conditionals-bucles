'''Ejercicio 2: Aprobado o reprobado Crea un programa que reciba la calificación de un estudiante (0 a 100) e indique si está aprobado (60 o más) o reprobado (menos de 60).'''

while True:     #Se pide la calificacion
    try:
        grade = float(input('Cual es tu calificacion? (0-100):'))
        if grade >= 0 and grade <= 100:  #Si cumple el rango, se sale del ciclo
            break
        print(f'El numero {grade} no esta dentro del rango de cero a cien')
    except Exception as e:
        print('Error', e)
        
if grade < 60:    #Se valida si aprueba o reprueba
    print(f'Usted ha reprobado porque su calificacion "{round(grade, 1)}" no logro los 60 requeridos')
else:
    print(f'Felicidades! Aprobaste el curso')