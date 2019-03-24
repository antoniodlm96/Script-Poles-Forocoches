from selenium import webdriver
import re
import random
import time

str_hilo = "https://www.forocoches.com/foro/showthread.php?t="
txt_poles = [
             'https://4.bp.blogspot.com/-JkGtS0U5crI/WAE3MpJmZbI/AAAAAAAAB_A/BPP_RZmRFBM6PuJRkQj9Px7lENCmXKHMQCLcB/s400/POLE.gif',
             'https://1.bp.blogspot.com/-BP5-wenGxp4/V2sFtZASGeI/AAAAAAAABvU/qJzx29nCK3kar9UQ83FtPGh_4ZZC8nllACLcB/s400/pole.gif',
             'https://1.bp.blogspot.com/-OUVPCbbm-8Q/V2qVZCE_PII/AAAAAAAABn0/4ERMOw2oI-wrSxBqD05u-0mMPEb5wN67ACLcB/s400/pole%2B2.gif',
             'https://3.bp.blogspot.com/-Q4hcyCCWegQ/V2qVe3t17ZI/AAAAAAAABoM/pqyHBJonY1MMdTb50eKENBpReyR8_1j3gCLcB/s400/pole%2B5.jpg',
             'https://3.bp.blogspot.com/-QK8O44MTsxI/V2qVjXVvFlI/AAAAAAAABoc/omKrdPUest42qM29U9_lZqhDG3Kzz9OjQCLcB/s400/pole.gif',
             'https://4.bp.blogspot.com/-jJ2H3STo-gY/V2P2Ax0oAeI/AAAAAAAABjQ/YfmtS2qSPBABoMNLSWZhvoLmONQWbgIPgCLcB/s400/pole.gif',
             'https://4.bp.blogspot.com/-A_4FlhvOGLo/VsscaeVYaII/AAAAAAAABGE/C-B4qesxn90/s400/aQsjMyM.gif',
             'https://4.bp.blogspot.com/-mVbjNWPTzb4/VssSsSiZNrI/AAAAAAAABFw/xjG4V8QBHlk/s400/Q0KYZLf.gif',
             'https://4.bp.blogspot.com/-YzxP0qCx9Nc/Vsr8soi7bJI/AAAAAAAABE4/oOt47S0pV0c/s400/j35dJqr.gif',
             'https://1.bp.blogspot.com/-cByk0cv8iUo/VsryaBgpfHI/AAAAAAAABEU/lJ9J_55FHKI/s400/SYKYBVE.gif',
             'https://1.bp.blogspot.com/-JhWQPrwcNGU/VroEuK4igvI/AAAAAAAAAv4/oPWjCXBOnFo/s400/2cxj8ti.gif',
             'https://1.bp.blogspot.com/-YStjABOz_94/VroE58VtZ6I/AAAAAAAAAwI/dm1gQhvVCTY/s400/2e3bfyq.gif',
             'https://1.bp.blogspot.com/-RMhLexwJWq0/VroFY6TZLpI/AAAAAAAAAwY/tUtkZVzxOzs/s400/2po324p.gif',
             'https://2.bp.blogspot.com/-yDpPdSQ0pZw/VroHnh9QKyI/AAAAAAAAAxg/W-PHkgtGSm4/s400/GhCzU.gif',
             'https://3.bp.blogspot.com/-R3jsnEQhFF4/VroIoMD1uCI/AAAAAAAAAyA/jIVwRQ2PZ_U/s400/neeww5.gif',
             'https://3.bp.blogspot.com/-1sWLelEJ7kU/VroIVPZcqRI/AAAAAAAAAxw/ArVBkXBzOaY/s400/ja9k7a.gif',
             'https://3.bp.blogspot.com/-9rxSgzATvMM/VroJzthHs9I/AAAAAAAAAyU/k-P9mxSuMjs/s400/vhvcpnvvs4kg.gif']

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

        titulo =  driver.find_element_by_xpath("//span[@class = 'cmega']")
        if "serio" not in titulo.text and "Serio" not in titulo.text:

            """
            area_escribir = driver.find_element_by_name("message")
            area_escribir.send_keys(str(random.choice(txt_poles)))
            area_escribir.send_keys(Keys.LEFT)
            area_escribir.send_keys(Keys.LEFT)
            area_escribir.send_keys(Keys.LEFT)
            area_escribir.send_keys(Keys.LEFT)
            area_escribir.send_keys(Keys.LEFT)
            """

            boton_enviar_imagen = driver.find_element_by_id("vB_Editor_QR_cmd_insertimage")
            boton_enviar_imagen.click()
            alert = driver.switch_to.alert
            alert.send_keys(random.choice(txt_poles))
            alert.accept()
            boton_enviar = driver.find_element_by_xpath("//input[@value = 'Enviar Respuesta']")
            boton_enviar.click()
            print("Pole exitosa!!1")
            time.sleep(29)

    except:
        print("No hay hilos donde hacer poles :(")

driver.close()
