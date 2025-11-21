from logic.NoticiasUltimaHora import ultimaHora
from logic.NoticiasIA import inteligenciaArtificial
from logic.NoticiasNegocios import negocioAndStartupSTech
from logic.NoticiasCiberseguridad import ciberseguridad
from logic.NoticiasHardwareGadgets import hardwareAndGadgets
from utils.MyDriver import iniciarChromeDriver


def main():

    # Iniciamos nuestro driver
    driver = iniciarChromeDriver()

    salir = True
    while salir:
        try: # INICIO DEL BLOQUE DE SEGURIDAD GENERAL

            print("\n\n")
            print("=" * 50)
            print("\t...::: MENÚ DE OPCIONES :::...")
            print("=" * 50)

            print("""
              1. 🔥 Última Hora / Hoy
              2. 🤖 Inteligencia Artificial (IA)
              3. 🔒 Ciberseguridad
              4. 📱 Hardware y Gadgets
              5. 💼 Negocio y Startups Tech
              6. ❌ Salir
              """)
            opcion = input("Digite una opción -> ")
            match opcion:
                case '1':
                   ultimaHora(driver)
                case '2':
                   inteligenciaArtificial(driver)
                case '3':
                    ciberseguridad(driver)
                case '4':
                    hardwareAndGadgets(driver)
                case '5':
                    negocioAndStartupSTech(driver)
                case '6':
                    print("¡Gracias por usar mi programa! :)\n¡Vuelva pronto!")
                    salir = False
                case _:
                    print("\n\t[-] ¡Opción no válida! Intente de nuevo...")

        except Exception as e:
            # Manejo de cualquier excepción que no haya sido capturada dentro de las funciones de noticias
            print("\n\n[-] ¡HA OCURRIDO UN ERROR INESPERADO EN EL PROGRAMA PRINCIPAL!")
            print("[+] Por favor, inténtelo de nuevo...")


    driver.quit()
if __name__ == '__main__':
    main()