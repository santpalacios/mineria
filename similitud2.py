import math

f1 = input('INGRESA LA FRASE 1:\n')
f2 = input('INGRESA LA FRASE 2:\n')

listaF1 = f1.split()
listaF2 = f2.split()


listaUnida = list(set(listaF1 + listaF2))
print("Lista unida:\n", listaUnida)

F1 = [1 if palabra in listaF1 else 0 for palabra in listaUnida]
F2 = [1 if palabra in listaF2 else 0 for palabra in listaUnida]

sumaFraces = sum(f1 * f2 for f1, f2 in zip(F1, F2))


magnitud1 = math.sqrt(sum(f1  for f1 in F1))
magnitud2 = math.sqrt(sum(f2  for f2 in F2))
  
similitud = sumaFraces / (magnitud1 * magnitud2)*100


porcentaje = similitud 

print("frase 1:", F1)
print("frase 2:", F2)   
print(f"Similitud: {similitud:.2f}")
print(f"Similitud en porcentaje: {porcentaje:.2f}%")
