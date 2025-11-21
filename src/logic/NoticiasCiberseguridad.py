import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException



def ciberseguridad(driver):
    URL = 'https://es.wired.com/tag/ciberseguridad'
    TIMEOUT = 20 # Tiempo de espera de 20 segundos


    print(f"\n[*] Visitando la página '{URL}'")
    try:
        driver.get(URL) # Le pasasmos la URL para iniciar/cagar la página
    except WebDriverException as e:
        print(f"[-] Error al cargar la URL: {URL}. Detalles: {e}")
    time.sleep(3)


    print("[*] Buscando la noticia de hoy...")
    try:
        WebDriverWait(driver,TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/article/div[2]/div/div/div/section/div/div[1]/div/div/div[1]/div[2]/a/h3'))
        ).click()
    except TimeoutException:
        print(f"[-] Error: El elemento de la primera noticia no se encontró después de esperar {TIMEOUT} segundos.")
        print("Posibles causas: página cargando lentamente, XPath incorrecto o cambios en la estructura del sitio.")
        return
    except NoSuchElementException:
        print("[-] Error: No se pudo encontrar el elemento de la primera noticia (XPath incorrecto o página diferente).")
        return
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado al hacer clic en la noticia: {e}")
        return

    print("\n[*] Obteniendo Información de la noticia...")
    print("[*] Esto podría demorar unos segundos...")
    time.sleep(3)

    try:
        titulo = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/main/article/div[1]/header/div/div[1]/div[1]/h1'))
        ).text
        time.sleep(2)
        entradilla = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/div/main/article/div[1]/header/div/div[1]/div[2]/div[1]'))
        ).text
        time.sleep(2)
        print("\n\n\t\t...::: TÍTULO :::...")
        print(titulo.upper())
        print("\n\n\t\t...::: ENTRADILLA :::...")
        print(entradilla)


    except TimeoutException:
        print(f"[-] Error: No se pudo encontrar información sobre la noticia después de esperar {TIMEOUT} segundos.")
        print("[-] Posibles causas: La página puede haber cambiado su estructura o tardó demasiado en cargar.")
        return
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado al intentar extraer más información de la noticia: {e}")
        return

    salir = True
    while salir:
        opcion = input("¿Desea saber más de esta noticia? (s/n)--> ").lower()
        if opcion == 's':
            print("\n[*] Buscando el contenido del artículo...")
            try:
                contenedor_div = WebDriverWait(driver, TIMEOUT).until(
                    EC.presence_of_element_located((By.CLASS_NAME,'body__inner-container'))
                )

                parrafos = contenedor_div.find_elements(By.TAG_NAME,'p')

                # 3. Iterar solo sobre los párrafos encontrados y extraer su texto
                if parrafos:
                    print("\n\n\t\t...::: CONTENIDO DEL ARTÍCULO :::...")

                    for p in parrafos:
                        # Aseguramos que el párrafo tenga texto visible
                        if p.text.strip():
                            print() # Usamos un salto de línea
                            print(p.text)

            except TimeoutException:
                print(f"[-] Error: No se pudo encontrar el contenedor después de esperar {TIMEOUT} segundos.")
                print("[-] El contenedor puede no estar disponible o la página cambió su estructura.")
            except Exception as e:
                print(f"[-] Ocurrió un error al extraer los párrafos: {e}")
            break
        elif  opcion == 'n':
            salir = False
        else:
            print("\n[-] ¡Opción no válida! Por favor, ingrese 's' o 'n'.")

    print("\n\n\n\t\t==========FIN DE LA NOTICIA==========")