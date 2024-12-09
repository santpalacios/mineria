from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from io import BytesIO

palabras_eliminar = [
    'el', 'la', 'los', 'las', 'de', 'y', 'a', 'en', 'un', 'una', 'por', 'para', 'con', 'que','uno','dos',
    'no', 'es', 'como', 'más', 'menos', 'si', 'al', 'las', 'del', 'sobre', 'este', 'esta', 'entre','otro',
    'me', 'te', 'cuando', 'muy', 'también', 'ser', 'yo', 'tú', 'él', 'ella', 'nosotros', 'nosotras','fue',
    'ellos', 'ellas', 'te', 'se', 'ha', 'haber', 'hacer', 'esto', 'estos', 'esas', 'pero', 'o', 'todo',
    'todos', 'cual', 'en', 'con', 'su', 'sus', 'y', 'sí', 'aquel', 'aquella', 'aquellos', 'aquellas', 'mi',
    'mis', 'tu', 'tus', 'su', 'sus', 'nuestro', 'nuestros', 'nuestra', 'nuestras', 'desde'
]

def cargar_imagen_forma(url_imagen):
  img = Image.open(url_imagen)
  return img

imagen_foco = cargar_imagen_forma(r"C:\Users\santp\Desktop\8vo\veliz\imagen\imagen.png")
imagen_foco = imagen_foco.convert("L")
foco_array = np.array(imagen_foco)
foco_array = np.where(foco_array > 200, 255, 0)

driver = webdriver.Chrome()

try:
    driver.get("https://poe.com")

    google_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Continuar con Google")]'))
    )
    google_button.click()
    print("Se hizo clic en 'Continuar con Google'.")

    email_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "identifierId"))
    )
    email_field.send_keys("l211080120@iztapalapa.tecnm.mx")
    driver.find_element(By.ID, "identifierNext").click()
    print("Correo ingresado y siguiente clickeado.")

    password_field = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.NAME, "Passwd"))
    )
    password_field.send_keys("montserrat12")
    driver.find_element(By.ID, "passwordNext").click()
    print("Contraseña ingresada y siguiente clickeado.")

    input("Presiona Enter para continuar...")

    continue_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button//span[contains(text(), "Continuar")]'))
    )
    continue_button.click()
    print("Se hizo clic en 'Continuar'.")

    text_area = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "GrowingTextArea_textArea__ZWQbP"))
    )
    print("Área de texto encontrada.")

    preguntas = [
        "Resumen breve de Harry Potter",
        "¿Quien es dobby?",
        "¿Como mataron a dobby?",
        "¿Qué es la varita de sauco?",
        "¿Cuáles son los magos mas poderosos?"
    ]

    questions_text = ", ".join(preguntas)

    text_area.clear()
    text_area.send_keys(questions_text)
    text_area.send_keys(Keys.RETURN)  #da un enter


    time.sleep(10)

    response = requests.get(driver.current_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        texto = soup.get_text(separator=' ', strip=True).lower()

        palabras = texto.split()
        palabras_limpias = [palabra for palabra in palabras if palabra.isalpha() and palabra not in palabras_eliminar]
        texto_limpio = ' '.join(palabras_limpias)

        if not texto_limpio:
            raise ValueError("El texto limpio está vacío. No se puede generar la nube de palabras.")

        wordcloud = WordCloud(
            width=1400,
            height=1400,
            background_color='white',
            mask=foco_array,
            contour_color='black',
            contour_width=5
        ).generate(texto_limpio)

        plt.figure(figsize=(9, 9))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
    else:
        print(f"No se pudo obtener la página. Código de estado: {response.status_code}")

finally:
    input("Presiona Enter para cerrar el navegador...")
    driver.quit()