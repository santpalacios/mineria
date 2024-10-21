
import math

datos = [
    [150, 'Aprobada'],
    [250, 'Aprobada'],
    [350, 'Aprobada']
]

while True:
    nuevaCantidad = int(input('INGRESA LA CANTIDAD: '))
    
    suma = 0
    contar = 0
    for x in datos:  
      
            if x[1] == 'Aprobada':
                suma += x[0]
                contar += 1
    promedio = suma / contar
    
    sumaCuadrados = sum((i[0] - promedio) ** 2 for i in datos if i[1] == 'Aprobada')
    varianza = sumaCuadrados / contar
    desviacionEstandar = math.sqrt(varianza)
    umbral = promedio + desviacionEstandar * 1.5

    if nuevaCantidad > umbral:
        print('RECHAZADA')
        datos.append([nuevaCantidad, 'Rechazada'])
    else:
        print('APROBADA')
        datos.append([nuevaCantidad, 'Aprobada'])

    print('----------------------------------------')
    header = ['Cantidad', 'Estado','Promedio','Desviación Estándar','Umbral']
    print(f'{header[0]:<10} {header[1]:<10} {header[2]:<10} {header[3]:<10} {header[4]:<10}')
    print('----------------------------------------')

    for i in datos:
        print(f'{i[0]:<10} {i[1]:<10}' + f' {promedio:<10.2f} {desviacionEstandar:<10.2f} {umbral:<10.2f}')

    while True:
        continuar = input('¿DESEAS INGRESAR OTRA CANTIDAD? (S/N) ').lower()
        if continuar in ['s', 'n']:
            break
        else:
            print("Entrada no válida. Por favor, ingresa 's' para sí o 'n' para no.")

    if continuar == 'n':
        break
    