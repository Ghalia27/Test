from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_shipping_address(self, telephone, name, address, city, country,province, postcode):

        phone_xpath = "//input[@name='address[telephone]']"
        name_xpath = "//input[@name='address[full_name]']"
        address_xpath = "//input[@name='address[address_1]']"
        city_xpath = "//input[@name='address[city]']"
        postal_code_xpath = "//input[@name='address[postcode]']"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, phone_xpath))
        ).send_keys(telephone)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, name_xpath))
        ).send_keys(name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, address_xpath))
        ).send_keys(address)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, city_xpath))
        ).send_keys(city)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, postal_code_xpath))
        ).send_keys(postcode)

        self.select_country(country)
        self.select_province(province)

        continue_button = (By.XPATH, "//span[contains(text(),'Continue to payment')]")
        self.driver.find_element(*continue_button).click()

    def select_country(self, country_name):
        # Esperar a que el elemento de selección esté presente
        country_select_xpath = "//select[@id='address[country]']"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, country_select_xpath))
        )

        # Localizar el elemento de selección
        select_element = self.driver.find_element(By.XPATH, country_select_xpath)

        # Crear una instancia de Select y seleccionar el país
        select = Select(select_element)
        select.select_by_visible_text(country_name)

    def select_province(self, province_name):
        # Esperar a que el elemento de selección esté presente
        province_select_xpath = "//select[@id='address[province]']"
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, province_select_xpath))
        )

        # Localizar el elemento de selección
        select_element = self.driver.find_element(By.XPATH, province_select_xpath)

        # Crear una instancia de Select y seleccionar la provincia
        select = Select(select_element)
        select.select_by_visible_text(province_name)

    def fill_payment_information(self, card_number, expiry_date, cvv):
        self.driver.find_element(By.ID, "card-number").send_keys(card_number)
        self.driver.find_element(By.ID, "expiry-date").send_keys(expiry_date)
        self.driver.find_element(By.ID, "cvv").send_keys(cvv)
        place_order_button = (By.XPATH, "//button[contains(text(),'Place Order')]")
        self.driver.find_element(*place_order_button).click()

    def verify_order_success(self):
        success_message = (By.XPATH, "//h1[contains(text(),'Thank you for your order')]")
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(success_message)
        )