import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_shop_now(self):
        woman_section= (By.XPATH, "//*[@id='app']/div/main/div[2]/div/div[2]/a/span['Shop women']")
        WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable(woman_section)
        ).click()

    def add_product_to_cart(self, product_name, quantity, size, color):

        product_link = (By.XPATH, f"//a/span[contains(text(),'{product_name}')]")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(product_link)
        ).click()

        #//*[@id="app"]/div/main/div[3]/div[2]/div[2]/div/div[1]/div[2]/a/span
        #//*[@id="app"]/div/main/div[3]/div[2]/div[2]/div/div[2]/div[2]/a/span
        quantity_field = (By.XPATH, "//input[@name='qty']")
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(quantity_field)
        ).clear()
        self.driver.find_element(*quantity_field).send_keys(str(quantity))


        size_select=(By.XPATH, f"//a[contains(text(),'{size}')]")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(size_select)
        ).click()

        time.sleep(3)
        color_select=(By.XPATH, f"//div[@id='app']/div/main/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul/li/a[text()='{color}']")
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(color_select)
        ).click()

        time.sleep(3)
        add_to_cart_button = (By.XPATH, "//*[@id='productForm']/div/div/div[2]/button/span['ADD TO CART']")
        self.driver.find_element(*add_to_cart_button).click()

        continue_shop= (By.XPATH, f"//a[contains(text(), 'Continue Shopping')]")
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable(continue_shop)
        ).click()

        return_list = (By.XPATH, "//span[2]/a[contains(text(),'Women') and @href='/women']")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(return_list)
        ).click()


    def go_to_checkout(self):
        checkout_button = (By.XPATH, "//a[@href='/cart']")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(checkout_button)
        ).click()
        checkout_button2 = (By.XPATH, "//a/span[contains(text(),'CHECKOUT')]")
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(checkout_button2)
        ).click()