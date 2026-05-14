
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrgerPage:
    def __init__(self, driver):
        """
        Конструктор класса OrderPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        """
        Данные для формления товаров
        """
        self.fields = {
            'firstName': "Иван",
            'lastName': "Петров",
            'postalCode': "123456"
        }

    @allure.step("Заполнение формы для оформления товаров")
    def user_info(self):
        """
        Заполняет форму данными пользователя для оформления заказа.
        :param value: данные пользователя для оформления товаров
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажвтие на кнопку Continue")
    def making_order(self):
        """
        Нажимает на кнопку Continue для оформления заказа.
        """
        self.wait.until(
           EC. visibility_of_element_located((By.ID, "continue"))).click()

    @allure.step("Получение суммы заказанных товаров")
    def total_price(self):
        """
        Получает сумму оформленных товаров.
        """
        total = self.wait.until(EC. visibility_of_element_located((
            By.CLASS_NAME, "summary_total_label"))).text
        total_str = total.split()[-1]
        """
        Возввращвет сумму оформленных товаров.
        :return: str - текст с суммой товаров
        """
        return total_str
