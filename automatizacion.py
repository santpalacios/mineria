from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import subprocess
import time
import os


chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)


driver = uc.Chrome()
driver.get("https://www.gob.mx/curp/")
time.sleep(10)

misDatosTab = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Datos Personales')]")))
misDatosTab.click()
time.sleep(10)

nombres = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "nombre")))
nombres.clear()
nombres.send_keys('DIANA MONTSERRAT')
primerApe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='primerApellido']")))
primerApe.clear()
primerApe.send_keys('PALACIOS')
segundoApe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='segundoApellido']")))
segundoApe.clear()
segundoApe.send_keys('SANTIAGO')
selectDia = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'diaNacimiento')))
select = Select(selectDia)
select.select_by_visible_text('19')
time.sleep(5)
selectMes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mesNacimiento')))
select = Select(selectMes)
select.select_by_visible_text('06')
time.sleep(5)
primerApe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='selectedYear']")))
primerApe.clear()
primerApe.send_keys('2000')
sexo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sexo')))
select = Select(sexo)
select.select_by_visible_text('Mujer')
time.sleep(5)
estado= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'claveEntidad')))
select = Select(estado)
select.select_by_visible_text('Ciudad de México')
time.sleep(5)

buscar = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(@class, "btn btn-primary pull-right")]')))
buscar.click()
time.sleep(5)


imprimir = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'download')))
imprimir.click()
time.sleep(5)   

#directorio descargas
directorio_descargas = os.path.join(os.path.expanduser("~"), "Downloads")


time.sleep(5)

#archivo más reciente en el directorio de descargas
def obtener_archivo_mas_reciente(directorio):
    archivos = [os.path.join(directorio, f) for f in os.listdir(directorio)]

    archivos = [f for f in archivos if os.path.isfile(f)]

    return max(archivos, key=os.path.getmtime) if archivos else None


archivo_descargado = obtener_archivo_mas_reciente(directorio_descargas)

if archivo_descargado:

    try:
        subprocess.run(["open", archivo_descargado])
    except Exception as e:
        print(f"No se pudo abrir el archivo: {e}")
else:
    print("No se encontró ningún archivo descargado.")

time.sleep(30)
