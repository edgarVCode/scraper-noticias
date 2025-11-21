import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


def ultimaHora(driver):
    URL = "https://expansion.mx/ultimas-noticias"
    TIMEOUT = 20  # Tiempo de espera global de 20 segundos

    print(f"\n[*] Visitando la página '{URL}'")
    try:
        driver.get(URL) # Le pasasmos la URL para iniciar/cagar la página
    except WebDriverException as e:
        print(f"[-] Error al cargar la URL: {URL}. Detalles: {e}")
        return

    print("[*] Buscando la noticia de hoy...")

    try:
        # Espera a que el elemento esté presente antes de hacer clic
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[4]/main/div[2]/section[1]/ul/li/div/div/div/div/section/ul/li[1]/div/div[1]/a'))
        ).click()

    except TimeoutException:
        print(f"[-] Error: El elemento de la primera noticia no se encontró después de esperar {TIMEOUT} segundos.")
        print("[-] Posibles causas: página cargando lentamente, XPath incorrecto o cambios en la estructura del sitio.")
        return
    except NoSuchElementException:
        print(
            "[-] Error: No se pudo encontrar el elemento de la primera noticia (XPath incorrecto o página diferente).")
        return
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado al intentar buscar la noticia: {e}")
        return

    print("\n[*] Obteniendo Información de la noticia...")
    print("[*] Esto podría demorar unos segundos...")
    time.sleep(3)

    try:
        titulo = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'BlocksPage-headline'))
        ).text

        time.sleep(2)

        entradilla = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'BlocksPage-subHeadline'))
        ).text
        time.sleep(2)
        print("\n\n\t\t...::: TÍTULO :::...")
        print(titulo.upper())
        print("\n\n\t\t...::: ENTRADILLA :::...")
        print(entradilla)


    except TimeoutException:
        print(f"\n[-] Error: No se pudo encontrar información sobre la noticia después de esperar {TIMEOUT} segundos.")
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
                    EC.presence_of_element_located((By.CLASS_NAME, "BlocksArticleFirstItem-body"))
                )

                # Buscar párrafos
                parrafos = contenedor_div.find_elements(By.TAG_NAME, "p")

                if parrafos:
                    print("\n\n\t\t...::: CONTENIDO DEL ARTÍCULO :::...")
                    for p in parrafos:
                        if p.text.strip():  # Solo imprimir párrafos con contenido
                            print(f"\n{p.text}")
                else:
                    print("[-] No se encontraron párrafos en el artículo.")
                break
            except TimeoutException:
                print(
                    f"[-] Error: No se pudo encontrar el contenido del artículo después de esperar {TIMEOUT} segundos.")
                print("[-] El contenido puede no estar disponible o la página cambió su estructura.")
                break
            except Exception as e:
                print(f"[-] Ocurrió un error al extraer los párrafos: {e}")
                break

        elif opcion == 'n':
            salir = False

        else:
            print("\n[-] ¡Opción no válida! Por favor, ingrese 's' o 'n'.")

    print("\n\n\n\t\t==========FIN DE LA NOTICIA==========")