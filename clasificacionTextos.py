import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

def procesar_pagina(url, palabras_filtradas):
    print("\nVisitando:", url)
    palabras_contador = Counter()

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            pagina = BeautifulSoup(respuesta.text, 'html.parser')
            parrafos = pagina.find_all(['p', 'h2'])

            for parrafo in parrafos:
                texto = parrafo.get_text(strip=True)
                if texto:
                    palabras = re.findall(r'\w+', texto.lower())
                    for palabra in palabras:
                        if palabra not in palabras_filtradas:
                            palabras_contador[palabra] += 1
        else:
            print("Error al acceder a", url, ":", respuesta.status_code)
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud a", url, ":", e)

    return palabras_contador.most_common(15)

def calcular_similitud(lista1, lista2):

    palabras1 = {palabra for palabra, _ in lista1} 
    palabras2 = {palabra for palabra, _ in lista2[:5]}     
    
 
    comunes = palabras1 & palabras2
    total_palabras = len(palabras1)
    
  
    if total_palabras > 0:
        porcentaje_similitud = (len(comunes) / total_palabras) * 100* 3
    else:
        porcentaje_similitud = 0

    return len(comunes), porcentaje_similitud


urls = [
    "https://www.harmonhall.com/",
    "https://dianglish.com/",
    "https://www.interlingua.com.mx/"
]


palabras_filtradas = {'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del',
                      'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una',
                      'su', 'al', 'es', 'lo', 'como', 'más', 'pero', 'sus',
                      'le', 'ya', 'o', 'fue', 'este', 'ha', 'sí', 'porque',
                      'iztapalapa', 'col', 'cp', 's', 'te', 'tu', 'te', 'ti',
                      'inglã', 'â', 'os', 'mã', '55', 'sin'}


resultados = []
for url in urls:
    palabras_comunes = procesar_pagina(url, palabras_filtradas)
    resultados.append((url, palabras_comunes))


for i in range(len(resultados)):
    for j in range(len(resultados)):
        if i != j: 
            url1, palabras1 = resultados[i]
            url2, palabras2 = resultados[j]

            comunes, porcentaje = calcular_similitud(palabras1, palabras2)

            print(f"\nComparación entre {url1} y {url2}:")
            print(f"Palabras comunes: {comunes}")
            print(f"Porcentaje de similitud: {porcentaje:.2f}%")
