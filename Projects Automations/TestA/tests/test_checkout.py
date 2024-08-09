import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from webdriver_manager.chrome import ChromeDriverManager
from config.driver_setup import get_driver
class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver('chrome')

    def test_place_order(self):
        self.driver.get("https://demo.evershop.io/")
        self.driver.maximize_window()
        # Home Page
        home_page = HomePage(self.driver)
        home_page.click_sign_in()

        # Login Page
        login_page = LoginPage(self.driver)
        login_page.sign_in("rebazaghalia27@gmail.com", "70839462")

        # Product Page - Add 3 products to the cart
        product_page = ProductPage(self.driver)
        product_page.go_to_shop_now()
        product_page.add_product_to_cart("Nike court vision low", 2, "S", "White")
        product_page.add_product_to_cart("Nike odyssey react flyknit 2", 3, "S", "Black")
        product_page.add_product_to_cart("Nike drop-type premium", 1, "S", "White")
        product_page.go_to_checkout()
        # Checkout Page
        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_shipping_address("999999999","John Doe", "123 Test St", "Lima", "Algeria","Biskra", "10001")
        checkout_page.fill_payment_information("4111111111111111", "12/24", "123")
        checkout_page.place_order()

        # Assertions
        self.assertTrue(checkout_page.verify_order_success())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()