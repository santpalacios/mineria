import math 

listaEdad= [] 
listaPeso = []
listaAltura = []
listaSueldo = []
listaSexoM = []
listaSexoH = []
contador = 1

def CantidadPersonas():
    while True:
        try:
            personas = int(input('¿Cuántas personas agregarás?  '))
            if personas > 1:
                return personas
            else:
                print('La cantidad de personas debe ser mayor a 1. \n ')
        except ValueError:
            print('Por favor ingresa un número entero válido. \n ')
            
cantidad_personas = CantidadPersonas()
while(contador <= cantidad_personas):
    print(f' \n Persona {contador} ')
    
    edad = int(input( 'edad : '))
    listaEdad.append(edad)

    peso = float(input('peso: '))
    listaPeso.append(peso)

    altura = float(input('altura: '))
    listaAltura.append(altura)
    
    sueldo = float(input('sueldo :'))
    listaSueldo.append(sueldo)

    while True:
        sexo = input('Sexo (h/m): ').lower()
        print('\n')
        if sexo =='h':
            listaSexoH.append(1)
            listaSexoM.append(0)
            break
        elif sexo == 'm':
            listaSexoM.append(1)
            listaSexoH.append(0)
            break
        else:
            print('Ingresa un sexo válido (h para hombre, m para mujer).')
    contador = contador + 1

ArrayFinal =[listaAltura,listaEdad,listaSueldo,listaPeso,listaSexoH,listaSexoM]

def normalizar(ArrayFinal):
    for lista in ArrayFinal:
        minLista = min(lista)
        maxLista = max(lista)
        norm = [(y - minLista) / (maxLista - minLista) for y in lista]


        
        print(f'\nNormalización de lista: {lista}')
        for idx, (valor, valor_normalizado) in enumerate(zip(lista, norm), start=1):
            print(f'Persona {idx} -- valor: {valor:.2f} -- Normalización: {valor_normalizado:.2f}')



print('Normalización de edades: ')
normalizar([listaEdad])  
print('\n')
print('Normalización de pesos: ')
normalizar([listaPeso])  
print('\n')
print('Normalización de altura: ')
normalizar([listaAltura]) 
print('\n')
print('Normalización de Sueldo: ')
normalizar([listaSueldo])  
print('Normalización de Sexo: ')
print('Hombres:  Mujeres:')
for i in range(cantidad_personas):
    print(f'Persona {i+1} -- {listaSexoH[i]} -- {listaSexoM[i]}')


