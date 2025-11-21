import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


def inteligenciaArtificial(driver):
    URL = 'https://es.wired.com/tag/inteligencia-artificial'
    TIMEOUT = 20  # Tiempo de espera de 20 segundos

    print(f"\n[*] Visitando la página '{URL}'")
    try:
        driver.get(URL) # Le pasamos el URL de la página a Google
    except WebDriverException as e:
        print(f"[-] Error al cargar la URL: {URL}. Detalles: {e}")
        return


    print("[*] Buscando la noticia de hoy...")
    try:
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[2]/div/div/main/article/div[2]/div/div/div/section/div/div[1]/div/div/div[1]/div[2]/a/h3'))
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
        print(f"[-] Ocurrió un error inesperado al hacer clic en la noticia: {e}")
        return

    print("\n[*] Obteniendo información de la noticia...")
    print("[*] Esto podría demorar unos segundos...")
    time.sleep(3)

    try:
        titulo = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/main/article/div[1]/header/div/div[1]/div[1]/h1"))
        ).text

        entradilla = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[2]/div/div/main/article/div[1]/header/div/div[1]/div[2]/div[1]"))
        ).text

        print("\n\n\t\t...::: TÍTULO :::...")
        print(titulo.upper())
        print("\n\n\t\t...::: ENTRADILLA :::...")
        print(entradilla)


    except TimeoutException:
        print(f"\n[-] Error: No se pudo encontrar información sobre la noticia después de esperar {TIMEOUT} segundos.")
        print("[-] La página puede haber cambiado su estructura o tardó demasiado en cargar.")
        return
    except Exception as e:
        print(f"[-] Ocurrió un error al extraer más información de la noticia: {e}")
        return


    salir = True
    while salir:
        opcion = input("¿Desea saber más sobre esta noticia? (s/n)--> ").lower()
        if opcion == 's':
            print("\n[*] Buscando el contenido del artículo...")
            try:
                # El XPath para el último DIV contenedor
                XPATH_DIV = "//div[@class='body__inner-container']"

                # 1. Localizar SOLO el último DIV contenedor
                contenedor_div = WebDriverWait(driver, TIMEOUT).until(
                    EC.presence_of_element_located((By.XPATH, XPATH_DIV))
                )

                elementos_a_extraer = contenedor_div.find_elements(
                    By.XPATH,
                    ".//*[self::p or self::h2]"
                )

                # 3. Iterar sobre la lista combinada y extraer el texto
                if elementos_a_extraer:
                    print("\n\n\t\t...::: CONTENIDO DEL ARTÍCULO :::...")

                    for elemento in elementos_a_extraer:
                        texto = elemento.text.strip()
                        tag = elemento.tag_name

                        # Aseguramos que el elemento tenga texto visible
                        if texto:
                            if tag == 'h2': # Imprimimos los subtítulos
                                print(f"\n\t\t{texto.upper()}")
                            else:
                                print(f"\n{texto}") # Imprimimos los párrafos
                else:
                    print("No se encontraron párrafos ni encabezados en el artículo.")

                break
            except TimeoutException:
                print(f"[-] Error: No se pudo encontrar el contenido del artículo después de esperar {TIMEOUT} segundos.")
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