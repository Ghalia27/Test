from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.XPATH, "//*[@id='app']/div/div[2]/div[3]/div[3]/a")

    def click_sign_in(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_button)
        ).click()