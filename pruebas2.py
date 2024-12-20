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

# Inicia el navegador con las opciones configuradas
driver = webdriver.Firefox(options=firefox_options)

# Ocultar `webdriver` en JavaScript
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# URL de inicio
driver.get("https://mail.google.com/")
time.sleep(random.uniform(8, 12))

# Ingresa el correo electrónico
correo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
correo.send_keys('l211080120@iztapalapa.tecnm.mx')
time.sleep(5)

# Haz clic en "Siguiente"
bttnNex = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
bttnNex.click()
time.sleep(random.uniform(4, 6))

input("Por favor, resuelve el captcha y presiona Enter para continuar...")

# Ingresa la contraseña
contraseña = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'Passwd')))
contraseña.send_keys('montserrat12')
time.sleep(15)

# Haz clic en "Siguiente"
bttnLogin = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.BqKGqe.Jskylb.TrZEUc.lw1w4b')))
bttnLogin.click()
time.sleep(random.uniform(8, 12))


#primer correo
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

#regresar a la bandeja de entrada
bandejaEntrada = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@data-tooltip="Recibidos"]'))
)
bandejaEntrada.click()
time.sleep(15)



# Asegúrate de que el segundo correo esté en la vista y hacer clic en él
segundoCorreo = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//tr[contains(@class, "zA")])[2]'))
)

# Desplazar al segundo correo y hacer clic
driver.execute_script("arguments[0].scrollIntoView(true);", segundoCorreo)
time.sleep(1)
ActionChains(driver).move_to_element(segundoCorreo).click().perform()

time.sleep(5)

contenidoCorreo = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//td[contains(@style, "font-family:Roboto")]'))
)

textoCorreo2 = contenidoCorreo.text.strip()
