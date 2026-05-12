
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver):
        """
       Конструктор класса MainPage.

       :param driver: WebDriver — объект драйвера Selenium.
       """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товаров в корзину")
    def add_product(self):
        """
        Добавляет товары в корзину.
        """
        self.wait.until(EC. element_to_be_clickable((
          By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))).click()
        self.wait.until(EC. element_to_be_clickable((
          By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        self.wait.until(EC. element_to_be_clickable((
          By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))).click()

    @allure.step("Переход в корзину")
    def cart_link(self):
        """
        Переходит в корзину.
        """
        self.wait.until(EC. element_to_be_clickable((
          By.CLASS_NAME, "shopping_cart_link"))).click()
