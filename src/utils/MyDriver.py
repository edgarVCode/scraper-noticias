import os
import platform

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from webdriver_manager.chrome import ChromeDriverManager


def iniciarChromeDriver():
    try:
        # Instalar el driver de Chrome automáticamente con fix para macOS
        driver_path = ChromeDriverManager().install()

        if platform.system() == 'Darwin':  # macOS
            if 'chromedriver-mac' in driver_path and not driver_path.endswith('chromedriver'):
                # Buscar el ejecutable real en la carpeta
                base_dir = os.path.dirname(driver_path)
                possible_path = os.path.join(base_dir, 'chromedriver')
                if os.path.exists(possible_path):
                    driver_path = possible_path

        service = Service(driver_path)

        options = webdriver.ChromeOptions()

        # --- Opciones Básicas ---
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")

        # --- Deshabilitar detección de automatización ---
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_settings.popups": 0,
        }
        options.add_experimental_option("prefs", prefs)

        if True:
            options.add_argument("--headless=new")

        # Inicializar el Driver
        driver: Chrome = webdriver.Chrome(options=options)

        # Ejecutar script para ocultar webdriver property (CRÍTICO)
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                       Object.defineProperty(navigator, 'webdriver', {
                           get: () => undefined
                       });

                       // Otros trucos para evasión
                       Object.defineProperty(navigator, 'plugins', {
                           get: () => [1, 2, 3, 4, 5]
                       });

                       Object.defineProperty(navigator, 'languages', {
                           get: () => ['es-MX', 'es', 'en-US', 'en']
                       });

                       window.chrome = {
                           runtime: {}
                       };

                       Object.defineProperty(navigator, 'permissions', {
                           get: () => ({
                               query: () => Promise.resolve({state: 'denied'})
                           })
                       });
                   '''
        })

        print("[+] Driver iniciado correctamente")
        return driver


    except Exception as e:
        return f"[-] Hubo un error al iniciar Driver: {e}"
        raise

