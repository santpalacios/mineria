import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import random
import re
from collections import Counter

def obtener_paginas(url, visitados, profundidad_actual, profundidad_maxima, palabras_contador, palabras_filtradas):
    if url in visitados or profundidad_actual > profundidad_maxima:
        return


    visitados.append(url)
    print("Visitando: ", url, "         ---Profundidad: ", profundidad_actual, "---")

    try:
        time.sleep(random.uniform(1, 3))

        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            pagina = BeautifulSoup(respuesta.text, 'html.parser')
            parrafos = pagina.find_all(['p', 'h2'])

            dominio_base = urlparse(url).netloc

            extensiones_no_permitidas = {'.pdf', '.jpg', '.jpeg', '.png', '.gif', '.zip', '.rar', '.doc', '.docx',
                                         '.xls', '.xlsx'}

         
            for parrafo in parrafos:
                texto = parrafo.get_text(strip=True)
                if texto:
                    palabras = re.findall(r'\w+', texto.lower())
                    for palabra in palabras:
                        if palabra not in palabras_filtradas:  
                            palabras_contador[palabra] += 1

            enlaces = pagina.find_all('a', href=True)
            for enlace in enlaces:
                url_completa = urljoin(url, enlace['href'])
                dominio_enlace = urlparse(url_completa).netloc

                if dominio_enlace == dominio_base:
                    if not any(url_completa.endswith(ext) for ext in extensiones_no_permitidas):
                        if 'googtrans' not in url_completa:
                            print(url_completa)
                            obtener_paginas(url_completa, visitados, profundidad_actual + 1, profundidad_maxima, palabras_contador, palabras_filtradas)
        else:
            print("Error al acceder a", url, ":", respuesta.status_code)
    except requests.exceptions.RequestException as e:
        print("Error al hacer la solicitud a", url, ":", e)

url_base = "https://nermil.com.mx/?menu=inicio"
visitados = []
profundidad_maxima = 1
palabras_contador = Counter()
palabras_filtradas = {'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 
                      'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 
                      'su', 'al', 'es', 'lo', 'como', 'más', 'pero', 'sus', 
                      'le', 'ya', 'o', 'fue', 'este', 'ha', 'sí', 'porque', 
                      'iztapalapa','col','cp'}

obtener_paginas(url_base, visitados, 0, profundidad_maxima, palabras_contador, palabras_filtradas)

palabrasPopulares = palabras_contador.most_common(5)
print("\nLas 5 palabras más comunes y su frecuencia son:")
for palabra, frecuencia in palabrasPopulares:
    print(f"{palabra}: {frecuencia}")
