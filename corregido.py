listaEdad= [] 
listaPeso = []
listaAltura = []
listaSueldo = []
listaSexoM = []
listaSexoH = []
listaColumnaSexo = [listaSexoH, listaSexoM]
contador = 1

personas = int(input('Cuantas personas agregarás? '))
while(contador <= personas):
    edad = int(input('edad: '))
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

def normalizar(lista):
    minLista = min(lista)
    maxLista= max(lista)
    contadorPersonas=0
    lista.sort()
    for i in lista:
        contadorPersonas +=1
        try:
            norm = (i - minLista) / (maxLista - minLista) 
        except ZeroDivisionError:
            #print('division entre 0 no permitida')
            return 0
        finally:
            print(f'Persona {contadorPersonas}--valor: {i:.2f} -- Normalizacion : {norm}')



print('Normalizacion de edades: ')
normalizar(listaEdad)
print('\n')
print('Normalizacion de pesos: ')
normalizar(listaPeso)
print('\n')
print('Normalizacion de altura: ')
normalizar(listaAltura)
print('\n')
print('Normalizacion de Sueldo: ')
normalizar(listaSueldo)
print('\n')
print('Normalización de Sexo:')
for i in range(personas):  
    hombre = listaColumnaSexo[0]  # Accede a listaSexoH
    mujer = listaColumnaSexo[1]
    print(f'Persona { i + 1} --hombre  --mujer \n             {hombre[i]}         {mujer[i]}')

