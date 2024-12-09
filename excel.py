import pandas as pd
import mysql.connector
import math

db_config = {
    'user': 'root',
    'password': 'montserrat12',
    'host': 'localhost',
    'database': 'cupidcode'
}

try:
    conn = mysql.connector.connect(**db_config)
    query = "SELECT * FROM veliz;"
    df_db = pd.read_sql(query, conn)
finally:
    conn.close()

excel_file_path = r"C:\Users\santp\Desktop\excel\PROYECTO VELIZ.xlsx"
df_excel = pd.read_excel(excel_file_path)

lista_db = [palabra for frase in df_db.astype(str).values.flatten() for palabra in frase.split()]
lista_excel = df_excel.astype(str).values.flatten().tolist()


lista_unida = list(set(lista_db + lista_excel))


F1 = [1 if palabra in lista_db else 0 for palabra in lista_unida]
F2 = [1 if palabra in lista_excel else 0 for palabra in lista_unida]


suma_frases = sum(f1 * f2 for f1, f2 in zip(F1, F2))
magnitud1 = math.sqrt(sum(f1 ** 2 for f1 in F1))
magnitud2 = math.sqrt(sum(f2 ** 2 for f2 in F2))

similitud = (suma_frases / (magnitud1 * magnitud2) * 100) if magnitud1 and magnitud2 else 0


print("\nLista DB (palabras):", lista_db)
print("\nLista Excel (palabras):", lista_excel)
print("\nLista unida:", lista_unida)
print("\nF1 (Base de datos):", F1)
print("\nF2 (Excel):", F2)
print(f"\nSimilitud: {similitud:.2f}%")