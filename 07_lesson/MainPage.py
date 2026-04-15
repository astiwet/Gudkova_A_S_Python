
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self):
        self.wait.until(EC. element_to_be_clickable((
          By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()
        self.wait.until(EC. element_to_be_clickable((
          By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        self.wait.until(EC. element_to_be_clickable((
          By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))).click()
           
    def cart_link(self):
        self.wait.until(EC. element_to_be_clickable((
          By.CLASS_NAME, "shopping_cart_link"))).click()
    