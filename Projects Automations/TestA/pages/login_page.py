from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.NAME, "email")
        self.password_field = (By.NAME, "password")
        self.create_account_button = (By.XPATH, "//*[@id='loginForm']/div[2]/button/span")

    def sign_in(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_field)
        ).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.create_account_button).click()