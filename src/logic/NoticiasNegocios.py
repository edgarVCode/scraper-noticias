import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

def negocioAndStartupSTech(driver):
    URL = 'https://es.wired.com/negocios'
    TIMEOUT = 20 # Tiempo de espera de 20 segundos

    print(f"\n[*] Visitando la página 'https://es.wired.com/negocios'")
    try:
        driver.get(URL)
    except WebDriverException as e:
        print(f"Error al cargar la URL '{URL}'. Detalles: {e}")
        return

    print("[*] Buscando la noticia de hoy...")
    try:
        # Esperar hasta que el elemento esté presente antes de hacer clic
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/main/div[2]/div[1]/div/div/div/div[2]/div[2]/a/h3'))
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

    print("\n[+] Obteniendo información de la noticia...")
    print("[*] Esto podría demorar unos segundos...")
    time.sleep(3)

    try:
        titulo = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div/main/article/div[1]/header/div/div[1]/div[1]/h1'))
        ).text

        entradilla = WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/main/article/div[1]/header/div/div[1]/div[2]/div[1]'))
        ).text

        print(f"\n\n\t\t...::: TÍTULO :::...")
        print(titulo.upper())
        print(f"\n\n\t\t...::: ENTRADILLA :::...")
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
                # Buscamos el DIV con la clase 'body__inner-container'
                XPATH_DIV = "//div[@class='body__inner-container']"

                # Localizar SOLO el primer DIV contenedor encontrado
                contenedor_div = WebDriverWait(driver, TIMEOUT).until(
                    EC.presence_of_element_located((By.XPATH, XPATH_DIV))
                )

                elementos_a_extraer = contenedor_div.find_elements(
                    By.XPATH,
                    ".//*[self::p or self::h2]"
                )


                # 3. Iterar sobre la lista combinada y aplicar formato
                if elementos_a_extraer:
                    print("\n\n\t\t...::: CONTENIDO DEL ARTÍCULO :::...")

                    for elemento in elementos_a_extraer:
                        texto = elemento.text.strip()
                        tag = elemento.tag_name

                        # Aseguramos que el elemento tenga texto visible
                        if texto:
                            # Aplicar formato especial si es un H2
                            if tag == 'h2':
                                print(f"\n\t\t{texto.upper()}")
                            else:
                                print(f"\n{texto}") # Imprimimos los párrafos

                else:
                    print("No se encontraron párrafos ni encabezados en el contenedor.")

                break

            except TimeoutException:
                print(
                    f"[-] Error: No se pudo encontrar el contenido del artículo después de esperar {TIMEOUT} segundos.")
                print("[-] El contenido puede no estar disponible o la página cambió su estructura.")
                break
            except Exception as e:
                print(f"[-] Ocurrió un error al extraer el contenido: {e}")
                break

        elif opcion == 'n':
            salir = False

        else:
            print("\n[-] ¡Opción no válida! Por favor, ingrese 's' o 'n'.")

        print("\n\n\n\t\t==========FIN DE LA NOTICIA==========")