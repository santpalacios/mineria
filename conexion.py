import mysql.connector
from mysql.connector import Error
from itertools import combinations


def soporte(productos, compras):
    suma_repeticiones = sum(1 for compra in compras if productos.issubset(set(compra)))
    return suma_repeticiones / len(compras)


def filtrar_inservibles(productos, soporte_minimo, compras):
    return {cproductos: cantidad for cproductos, cantidad in productos.items() if soporte(cproductos, compras) >= soporte_minimo}
                                                                ##############

def reglas(compras_filtradas, confianza_minima, compras):
    reglas = []
    for ccompra in compras_filtradas.keys():  ###################
        if len(ccompra) > 1:
            for producto in ccompra:
                antecedente = ccompra - frozenset([producto])
                #if len(antecedente) > 0:
                confianza = soporte(ccompra, compras) / soporte(antecedente, compras)
                if confianza >= confianza_minima:
                    reglas.append((antecedente, frozenset([producto]), confianza))
    return reglas

try:
    conexion = mysql.connector.connect(
        host='localhost',
        database='subconjuntos',
        user='root',
        password='montserrat12'
    )

    if conexion.is_connected():
        print("Conexión exitosa")

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM vw_matriz;")
        resultados = cursor.fetchall()

        compras = []  
        for fila in resultados:
            x = fila[1]
            compras.append(frozenset(x.split(',')))

        soporte_minimo = 0.3  # soporte mínimo del 20%
        confianza_minima = 0.8  # confianza mínima del 50%
        
        # Generar compras de tamaño 1 hasta el tamaño máximo de items en las transacciones
    compras_filtradas = {}
    compra_mayor = max(len(compra) for compra in compras)
    combinaciones_compras = {}
    for i in range(1, compra_mayor+1):

        for compra in compras:
             for combinaciones in combinations(set(compra), i):
                 combinacion = frozenset(combinaciones)
                 if combinacion in combinaciones_compras:
                    combinaciones_compras[combinacion] += 1
                 else:
                     combinaciones_compras[combinacion] = 1

    filtrados = filtrar_inservibles(combinaciones_compras, soporte_minimo, compras)
    compras_filtradas.update(filtrados)


        # Generar reglas
    reglas = reglas(compras_filtradas, confianza_minima, compras)

        # Mostrar resultados
    print("compras frecuentes:")
    for combinacion, cantidad in compras_filtradas.items():
        print(set(combinacion), 'soporte= ', soporte(combinacion, compras))
    print("\nreglas:")
    for antecedente, consecuente, confianza in reglas:
        print(set(antecedente), '->', set(consecuente), 'Confianza =', confianza)
    print(reglas)
    print(filtrados)
    print(compras_filtradas)
    print(combinaciones_compras)
    print("///////////////////////////////////////////////")
    print(resultados)

except Error as e:
    print(f"Error al conectar a MySQL: {e}")

finally:
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada")