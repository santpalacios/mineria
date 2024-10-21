import math

def obtener_sexo():
    while True:
        sexo = input('Sexo (h/m): ').lower()
        if sexo == 'h':
            return 1, 0  
        elif sexo == 'm':
            return 0, 1  
        else:
            print('Ingresa un sexo válido (h para hombre, m para mujer).')

def normalizar(lista):
    minLista = min(lista)
    maxLista = max(lista)
    if maxLista == minLista:
        return [0] * len(lista)
    return [(i - minLista) / (maxLista - minLista) for i in lista]

def calcular_distancia(edad, peso, altura, sueldo, sexo_h, sexo_m, edad_comparar, peso_comparar, altura_comparar, sueldo_comparar, sexo_h_comparar, sexo_m_comparar):
    return math.sqrt((edad - edad_comparar)**2 + (peso - peso_comparar)**2 + (altura - altura_comparar)**2 + (sueldo - sueldo_comparar)**2 + (sexo_h - sexo_h_comparar)**2 + (sexo_m - sexo_m_comparar)**2)


cantidad_personas = int(input('¿Cuántas personas agregarás? '))

listaEdades = []
listaPesos = []
listaAlturas = []
listaSueldos = []
listaSexosH = []
listaSexosM = []
listaStatus = []

for i in range(1, cantidad_personas + 1):
    print(f'Persona {i}')
    edad = int(input('Edad: '))
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    sueldo = float(input('Sueldo: '))
    sexo_h, sexo_m = obtener_sexo()
    status = input('Status (paga/no paga): ').lower()
    
    listaEdades.append(edad)
    listaPesos.append(peso)
    listaAlturas.append(altura)
    listaSueldos.append(sueldo)
    listaSexosH.append(sexo_h)
    listaSexosM.append(sexo_m)
    listaStatus.append(status)


paga_count = listaStatus.count('paga')
no_paga_count = listaStatus.count('no paga')

if paga_count > no_paga_count:
    status_comparar = 'paga'
else:
    status_comparar = 'no paga'

# Normalizar los datos
edad_normalizada = normalizar(listaEdades)
peso_normalizada = normalizar(listaPesos)
altura_normalizada = normalizar(listaAlturas)
sueldo_normalizada = normalizar(listaSueldos)

# Datos de la persona a comparar
print("\nValores de la persona a comparar:")
edad_comparar = int(input('Edad: '))
peso_comparar = float(input('Peso: '))
altura_comparar = float(input('Altura: '))
sueldo_comparar = float(input('Sueldo: '))
sexo_h_comparar, sexo_m_comparar = obtener_sexo()

# Normalizar los datos de la persona a comparar
edad_comparar = (edad_comparar - min(listaEdades)) / (max(listaEdades) - min(listaEdades))
peso_comparar = (peso_comparar - min(listaPesos)) / (max(listaPesos) - min(listaPesos))
altura_comparar = (altura_comparar - min(listaAlturas)) / (max(listaAlturas) - min(listaAlturas))
sueldo_comparar = (sueldo_comparar - min(listaSueldos)) / (max(listaSueldos) - min(listaSueldos))


listaPersonas = []
for i in range(cantidad_personas):
    edad = edad_normalizada[i]
    peso = peso_normalizada[i]
    altura = altura_normalizada[i]
    sueldo = sueldo_normalizada[i]
    sexo_h = listaSexosH[i]
    sexo_m = listaSexosM[i]
    status = listaStatus[i]
    distancia = calcular_distancia(edad, peso, altura, sueldo, sexo_h, sexo_m, edad_comparar, peso_comparar, altura_comparar, sueldo_comparar, sexo_h_comparar, sexo_m_comparar)
    listaPersonas.append([edad, peso, altura, sueldo, sexo_h, sexo_m, status, distancia])

listaPersonas.append([edad_comparar, peso_comparar, altura_comparar, sueldo_comparar, sexo_h_comparar, sexo_m_comparar, status_comparar, -1])


listaPersonas.sort(key=lambda x: x[7])


headers = ['Edad', 'Peso', 'Altura', 'Sueldo', 'Hombre', 'Mujer', 'Status', 'Distancia']
print('\nLista de personas ordenada por distancia:')
print(f"{headers[0]:<10} {headers[1]:<10} {headers[2]:<10} {headers[3]:<10} {headers[4]:<10} {headers[5]:<10} {headers[6]:<10} {headers[7]:<10}")
print("="*80)
for persona in listaPersonas:
    print(f"{persona[0]:<10.2f} {persona[1]:<10.2f} {persona[2]:<10.2f} {persona[3]:<10.2f} {persona[4]:<10} {persona[5]:<10} {persona[6]:<10} {persona[7]:<10.2f}")