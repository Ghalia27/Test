from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_driver(browser='chrome'):
    if browser.lower() == 'chrome':
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Navegador '{browser}' no soportado.")

    driver.maximize_window()
    return driver