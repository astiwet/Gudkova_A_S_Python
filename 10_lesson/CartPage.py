
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    def __init__(self, driver):
        """
       Конструктор класса CartPage.

       :param driver: WebDriver — объект драйвера Selenium.
       """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Получение списка товаров в корзине")
    def get_cart_items(self):
        """
        Получает список товаров в корзине.

        :param items = [str] — список товаров в корзине.
        """
        items = []
        cart_item_elements = self.driver.find_elements(By.CLASS_NAME,
                                                       'cart_item')
        for item in cart_item_elements:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name'
                                     ).text
            price = item.find_element(By.CLASS_NAME, 'inventory_item_price'
                                      ).text
            items.append({'name': name, 'price': price})
        """
        Возвращает полученный список товаров в корзине.
        :return: [str] — список товаров.
        """
        return items

    @allure.step("Переход к оформлению товаров")
    def checkout(self):
        """
        Переходит для оформления товаров в корзине.
        """
        self.wait.until(EC. visibility_of_element_located((By.ID, "checkout"))
                        ).click()
