import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

firefox_options = Options()
firefox_options.set_preference("dom.webdriver.enabled", False)
firefox_options.set_preference(
    "general.useragent.override", 
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36"
)

driver = webdriver.Firefox(options=firefox_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://mail.google.com/")
time.sleep(random.uniform(8, 12))

correo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
correo.send_keys('l211080120@iztapalapa.tecnm.mx')
time.sleep(5)

bttnNex = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
bttnNex.click()
time.sleep(random.uniform(4, 6))

input("Por favor, resuelve el captcha y presiona Enter para continuar...")

contraseña = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Passwd')))
contraseña.send_keys('montserrat12')
time.sleep(15)

bttnLogin = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b')))
bttnLogin.click()
time.sleep(random.uniform(8, 12))

# Primer correo
primerCorreo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '(//tr[contains(@class, "zA")])[1]'))
)

driver.execute_script("arguments[0].scrollIntoView(true);", primerCorreo)
time.sleep(1)
ActionChains(driver).move_to_element(primerCorreo).click().perform()
time.sleep(5)

contenedorCorreo = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//div[contains(@id, "main")]'))
)

etiquetai = contenedorCorreo.find_elements(By.TAG_NAME, "i")
textocorreo1 = [etiqueta.text.strip() for etiqueta in etiquetai]

# Regresar a la bandeja de entrada
bandejaEntrada = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@data-tooltip="Recibidos"]'))
)
bandejaEntrada.click()
time.sleep(15)

# Segundo correo
segundoCorreo = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//tr[contains(@class, "zA")])[2]'))
)

driver.execute_script("arguments[0].scrollIntoView(true);", segundoCorreo)
time.sleep(1)
ActionChains(driver).move_to_element(segundoCorreo).click().perform()
time.sleep(5)

contenidoCorreo2 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//td[contains(@style, "font-family:Roboto")]'))
)

textoCorreo2 = contenidoCorreo2.text.strip()


f1 = textocorreo1 
f2 = textoCorreo2.split()  


listaUnida = list(set(f1 + f2))  

F1 = [1 if palabra in f1 else 0 for palabra in listaUnida]
F2 = [1 if palabra in f2 else 0 for palabra in listaUnida]

sumaFraces = sum(f1 * f2 for f1, f2 in zip(F1, F2))

magnitud1 = math.sqrt(sum(f1 for f1 in F1))
magnitud2 = math.sqrt(sum(f2 for f2 in F2))
similitud = sumaFraces / (magnitud1 * magnitud2)


print("/////////////////////////////////////////////////")
print("PAGINA1: ", f1)
print("/////////////////////////////////////////////////")
print("PAGINA2: ", f2)
print("/////////////////////////////////////////////////")
print("Lista unida: ", listaUnida)
print("/////////////////////////////////////////////////")
print("frase 1:", F1)
print("frase 2:", F2)   
print(f"Similitud: {similitud:.2f}")
print(f"Similitud en porcentaje: {similitud*100:.2f}%")