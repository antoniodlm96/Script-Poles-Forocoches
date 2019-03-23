from selenium import webdriver
import re

str_hilo = "https://www.forocoches.com/foro/showthread.php?t="

driver = webdriver.Chrome()
driver.get("https://www.forocoches.com/foro/forumdisplay.php?f=2")
usuario = input("Usuario: ")
contrasena = input("Contraseña: ")
elemento_usuario = driver.find_element_by_xpath("//input[@value = 'Usuario']")
elemento_contrasena = driver.find_element_by_xpath("//input[@type = 'password']")
boton_login = driver.find_element_by_xpath("//input[@value = 'Acceder']")
elemento_usuario.send_keys(usuario)
elemento_contrasena.send_keys(contrasena)
boton_login.click()

while True:

    driver.get("https://www.forocoches.com/foro/forumdisplay.php?f=2")
    try:
        element = driver.find_element_by_xpath("//strong[text() = 0]")
        parent = element.find_element_by_xpath("./..")
        link = parent.get_attribute("href")
        p = re.compile(r'\d+')
        id_hilo = p.findall(link)[0]
        link_hilo = str_hilo + id_hilo
        driver.get(link_hilo)
        print(link_hilo)

        area_escribir = driver.find_element_by_name("message")
        area_escribir.send_keys("Pole automatica hecha con poles.py @LemonCat_")

        boton_enviar = driver.find_element_by_xpath("//input[@value = 'Enviar Respuesta']")
        boton_enviar.click()
        print("Pole exitosa!!1")

    except:
        print("No hay hilos donde hacer poles :(")

driver.close()
