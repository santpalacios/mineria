import math
import pandas as pd

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

Status = ['paga', 'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga', 'paga', 'no paga', 'paga', 
                'no paga']


def normalizar(lista):

    min_val = min(lista)
    max_val = max(lista)
    if max_val == min_val:
        return [0] * len(lista)
    return [(i - min_val) / (max_val - min_val) for i in lista]


edadNormalizada = normalizar(listaEdades)
pesoNormalizado = normalizar(listaPesos)
alturaNormalizada = normalizar(listaAlturas)
sueldoNormalizado = normalizar(listaSueldos)
sexoHNormalizado = normalizar(listaSexosH)


print('TABLA DE DATOS INICIALES')
df_tabla=pd.DataFrame({'Edad':listaEdades,'Peso':listaPesos,'Altura':listaAlturas,'Sueldo':listaSueldos,'Sexo H':listaSexosH,'Sexo M':listaSexosM,'Status':Status})
print(df_tabla)

print('TABLA DE DATOS NORMALIZADOS')
df_tabla_normalizada=pd.DataFrame({'Edad':edadNormalizada,'Peso':pesoNormalizado,'Altura':alturaNormalizada,'Sueldo':sueldoNormalizado,'Sexo H':listaSexosH,'Sexo M':listaSexosM})
print(df_tabla_normalizada)

#CREAR GRUPOS
cantidadGrupos = int(input('Ingrese la cantidad de grupos: '))
filasAleatorias = df_tabla_normalizada.sample(n=cantidadGrupos, random_state=1).index


df_tabla_normalizada['Grupo'] =0  
for i, fila in enumerate(filasAleatorias):
    df_tabla_normalizada.at[fila, 'Grupo'] = i + 1  

print('\nLista de personas con grupos asignados:')
print(df_tabla_normalizada)

#CALCULAR DISTANCIAS ENTRE GRUPOS
def calcularDistancias():
    for grupo in range(1, cantidadGrupos + 1):
     df_tabla_normalizada[f'Distancia_Grupo_{grupo}'] 

    df_grupo = df_tabla_normalizada[df_tabla_normalizada['Grupo'] != 0]
    df_sinGrupo = df_tabla_normalizada[df_tabla_normalizada['Grupo'] == 0]

    for filaSinGrupo in df_sinGrupo.iterrows():
       for filaGrupo in df_grupo.iterrows():
          grupo = filaGrupo['Grupo']
          distancias = math.sqrt((filaSinGrupo['Edad'] - filaGrupo['Edad'])**2 + 
                                 (filaSinGrupo['Peso'] - filaGrupo['Peso'])**2 + 
                                 (filaSinGrupo['Altura'] - filaGrupo['Altura'])**2 + 
                                 (filaSinGrupo['Sueldo'] - filaGrupo['Sueldo'])**2 + 
                                 (filaSinGrupo['Sexo H'] - filaGrupo['Sexo H'])**2 +
                                 (filaSinGrupo['Sexo M'] - filaGrupo['Sexo M'])**2
                                 )
          df_tabla_normalizada.at[filaSinGrupo, f'Distancia_Grupo_{grupo}'] = distancias