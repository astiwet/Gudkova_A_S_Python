

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AutorizationPage:
    def __init__(self, driver):
        """
       Конструктор класса AutorizationPage.

       :param driver: WebDriver — объект драйвера Selenium.
       """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы магазина")
    def open(self):
        """
        Открывает страницу магазина.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод имени пользователя: {term}")
    def autorization_login(self, term):
        """
        Вводит имя пользователя.
        :param term: str — имя пользователя.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(term)

    @allure.step("Ввод пароля пользователя: {term}")
    def autorization_pass(self, term):
        """
        Вводит пароль пользователя.
        :param term: str — пароль пользователя.
        """
        self.driver.find_element(By.ID, "password").send_keys(term)

    @allure.step("Нажатие на кнопку LOGIN")
    def login_button(self):
        """
        Нажимает на кнопку LOGIN для регистрации в магазине

        """
        self.wait.until(EC. element_to_be_clickable((By.ID, "login-button"))
                        ).click()
