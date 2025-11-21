import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


def hardwareAndGadgets(driver):
    URL = 'https://hardzone.es/'
    TIMEOUT = 20 # Tiempo de espera de 20 segundos

    print(f"\n[*] Visitando la página de: '{URL}'")
    try:
        driver.get(URL) # Le pasasmos la URL para iniciar/cagar la página
    except WebDriverException as e:
        print(f"[-] Error al cargar la URL '{URL}'. Detalles: {e}")
        return

    print("[*] Buscando la noticia de hoy...")
    try:
        # Esperar hasta que el elemento esté presente antes de hacer clic
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[3]/div[4]/div[3]/div/div[1]/section/div[1]/div/div/h2/a/span'))
        ).click()

    except TimeoutException:
        print(f"[-] Error: El elemento de la primera noticia no se encontró después de esperar {TIMEOUT} segundos.")
        return
    except NoSuchElementException:
        print(
            f"[-] Error: No se pudo encontrar el elemento de la primera noticia (XPath incorrecto o página diferente).")
        return
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado al intentar buscar la noticia: {e}")
        return
    time.sleep(2)

    print("\n[*] Obteniendo Información de la noticia...")
    print("[+] Esto podría demorar unos segundos...")
    time.sleep(3)

    try:
        titulo = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.CLASS_NAME, "post-article__title"))
        ).text

        time.sleep(2)

        entradilla = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[3]/div[4]/div[3]/div/div[2]/article/div[4]/div[2]/div[1]/p"))
        ).text

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
        opcion = input("¿Desea saber más sobre esta noticia? (s/n)--> ").lower()
        if opcion == 's':
            print("\n[*] Buscando el contenido del artículo...")

            try:
                # Localizar el contenedor principal del artículo.
                CONTENEDOR_ARTICULO_XPATH = "//article[contains(@class, 'post-article')]"

                contenedor_articulo = WebDriverWait(driver, TIMEOUT).until(
                    EC.presence_of_element_located((By.XPATH, CONTENEDOR_ARTICULO_XPATH))
                )

                elementos_a_extraer = contenedor_articulo.find_elements(
                    By.XPATH,
                    ".//*[self::p or self::h2]"
                )

                if elementos_a_extraer:
                    print("\n\n\t\t...::: CONTENIDO DEL ARTÍCULO :::...")

                    for elemento in elementos_a_extraer:
                        texto = elemento.text.strip()
                        tag = elemento.tag_name
                        # Aseguramos que el elemento tenga texto visible
                        if texto:
                            if tag == 'h2':  # Imprimimos los subtítulos
                                print(f"\n\t\t{texto.upper()}")
                            else:
                                print(f"\n{texto}")  # Imprimimos los párrafos
                        else:
                            print("No se encontraron párrafos ni encabezados en el artículo.")
                    break  # Salimos del bucle 'while'

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