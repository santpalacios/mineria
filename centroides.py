import math
import pandas as pd  

def obtener_sexo():
   
    while True:
        sexo = input('Sexo (h/m): ').lower()
        if sexo == 'h':
            sexo_h =1
            sexo_m =0
            return sexo_h, sexo_m
        elif sexo == 'm':
            sexo_h =0
            sexo_m =1
            return sexo_h, sexo_m
        else:
            print("Entrada inválida. Por favor ingrese 'h' para hombre o 'm' para mujer.")

def normalizar(lista):

    min_val = min(lista)
    max_val = max(lista)
    if max_val == min_val:
        return [0] * len(lista)
    return [(i - min_val) / (max_val - min_val) for i in lista]

def calcular_distancia(edad, peso, altura, sueldo, sexo_h, sexo_m, 
                       edad_comparar, peso_comparar, altura_comparar, 
                       sueldo_comparar, sexo_h_comparar, sexo_m_comparar):
    """
    Calcula la distancia euclidiana entre dos personas considerando sus 
    características normalizadas.
    """
    return math.sqrt((edad - edad_comparar)**2 + 
                     (peso - peso_comparar)**2 + 
                     (altura - altura_comparar)**2 + 
                     (sueldo - sueldo_comparar)**2 + 
                     (sexo_h - sexo_h_comparar)**2 + 
                     (sexo_m - sexo_m_comparar)**2)

# Listas pre-cargadas con datos
listaEdades = [22, 34, 45, 27, 31, 29, 40, 50, 60, 70, 
               25, 35, 55, 65, 75, 20, 30, 40, 50, 60, 
               32, 42, 52, 62, 72, 28, 38, 48, 58, 68]
listaPesos = [70.5, 80.2, 90.3, 60.4, 75.5, 85.6, 95.7, 
              65.8, 55.9, 45.0, 68.1, 78.2, 88.3, 58.4, 
              48.5, 72.6, 82.7, 92.8, 62.9, 52.0, 
              74.1, 84.2, 94.3, 64.4, 54.5, 76.6, 
              86.7, 96.8, 66.9, 56.0]
listaAlturas = [1.75, 1.80, 1.85, 1.60, 1.65, 1.70, 
                1.90, 1.95, 1.55, 1.50, 1.78, 1.83, 
                1.88, 1.63, 1.68, 1.73, 1.93, 1.98, 
                1.53, 1.48, 1.77, 1.82, 1.87, 1.62, 
                1.67, 1.72, 1.92, 1.97, 1.52, 1.47]
listaSueldos = [3000, 4500, 6000, 3500, 5000, 6500, 
                 4000, 5500, 7000, 7500, 3200, 4700, 
                 6200, 3700, 5200, 6700, 4200, 5700, 
                 7200, 7700, 3400, 4900, 6400, 3900, 
                 5400, 6900, 4400, 5900, 7400, 7900]
listaSexosH = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 
                0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 
                0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
listaSexosM = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 
                1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 
                1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
listaStatus = ['paga', 'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga']

# Normalización de los datos
edad_normalizada = normalizar(listaEdades)
peso_normalizado = normalizar(listaPesos)
altura_normalizada = normalizar(listaAlturas)
sueldo_normalizado = normalizar(listaSueldos)

print("\nValores de la persona a comparar:")
edad_comparar = int(input('Edad: '))
peso_comparar = float(input('Peso: '))
altura_comparar = float(input('Altura: '))
sueldo_comparar = float(input('Sueldo: '))
sexo_h_comparar, sexo_m_comparar = obtener_sexo()

# Normalizar la persona a comparar
status_comparar = 'paga' if listaStatus.count('paga') > listaStatus.count('no paga') else 'no paga'
edad_comparar_normalizada = (edad_comparar - min(listaEdades)) / (max(listaEdades) - min(listaEdades))
peso_comparar_normalizado = (peso_comparar - min(listaPesos)) / (max(listaPesos) - min(listaPesos))
altura_comparar_normalizada = (altura_comparar - min(listaAlturas)) / (max(listaAlturas) - min(listaAlturas))
sueldo_comparar_normalizado = (sueldo_comparar - min(listaSueldos)) / (max(listaSueldos) - min(listaSueldos))

# Generar lista de personas
listaPersonas = []
for i in range(len(listaEdades)):
    edad = edad_normalizada[i]
    peso = peso_normalizado[i]
    altura = altura_normalizada[i]
    sueldo = sueldo_normalizado[i]
    sexo_h = listaSexosH[i]
    sexo_m = listaSexosM[i]
    status = listaStatus[i]
    distancia = calcular_distancia(edad, peso, altura, sueldo, sexo_h, sexo_m, 
                                   edad_comparar_normalizada, peso_comparar_normalizado, 
                                   altura_comparar_normalizada, sueldo_comparar_normalizado, 
                                   sexo_h_comparar, sexo_m_comparar)
    listaPersonas.append([edad, peso, altura, sueldo, sexo_h, sexo_m, status, distancia])

# Agregar la persona a comparar
listaPersonas.append([edad_comparar_normalizada, peso_comparar_normalizado, altura_comparar_normalizada, 
                      sueldo_comparar_normalizado, sexo_h_comparar, sexo_m_comparar, status_comparar, -1])

# Ordenar por distancia
listaPersonas.sort(key=lambda x: x[7])

# Crear DataFrame y mostrar
df_personas = pd.DataFrame(listaPersonas, columns=['Edad', 'Peso', 'Altura', 'Sueldo', 'Hombre', 'Mujer', 'Status', 'Distancia'])

print('\nLista de personas ordenada por distancia:')
print(df_personas)

# Agrupar personas
cantidadGrupos = int(input('Cuantos grupos desea hacer: '))
filas_aleatorias = df_personas.drop(index=0).sample(n=cantidadGrupos, random_state=1).index

df_personas['Grupo'] = 0  # Inicializar columna de grupos
for i, fila in enumerate(filas_aleatorias):
    df_personas.at[fila, 'Grupo'] = i + 1  

print('\nLista de personas con grupos asignados:')
print(df_personas)


#se crean las columnas de distancia para cada grupo
for grupo in range(1, cantidadGrupos + 1):
    df_personas[f'Distancia_Grupo_{grupo}'] = float('nan')

def calcularDistanciasGrupos(df):
    # Filtrar filas con grupo asignado
    df_grupos = df[df['Grupo'] != 0]
    df_sin_grupo = df[df['Grupo'] == 0]
    
    # Calcular distancias euclidianas
    for _, fila_sin_grupo in df_sin_grupo.iterrows():
        for _, fila_grupo in df_grupos.iterrows():
            grupo = fila_grupo['Grupo']
            distancia = math.sqrt(
                (fila_sin_grupo['Edad'] - fila_grupo['Edad'])**2 +
                (fila_sin_grupo['Peso'] - fila_grupo['Peso'])**2 +
                (fila_sin_grupo['Altura'] - fila_grupo['Altura'])**2 +
                (fila_sin_grupo['Sueldo'] - fila_grupo['Sueldo'])**2 +
                (fila_sin_grupo['Hombre'] - fila_grupo['Hombre'])**2 +
                (fila_sin_grupo['Mujer'] - fila_grupo['Mujer'])**2
            )
            df.at[fila_sin_grupo.name, f'Distancia_Grupo_{grupo}'] = distancia


calcularDistanciasGrupos(df_personas)

# Asignar el grupo con la distancia mínima a cada fila sin grupo
for index, row in df_personas[df_personas['Grupo'] == 0].iterrows():
    distancias = row[[f'Distancia_Grupo_{grupo}' for grupo in range(1, cantidadGrupos + 1)]]
    grupo_min_distancia = distancias.idxmin().split('_')[-1]
    df_personas.at[index, 'Grupo'] = int(grupo_min_distancia)



# Seleccionar las columnas 'Grupo' y las columnas de distancias
columnas_a_imprimir = ['Grupo'] + [f'Distancia_Grupo_{grupo}' for grupo in range(1, cantidadGrupos + 1)]

print('\nLista de personas con distancias asignadas:')
print(df_personas[columnas_a_imprimir])
        
    
