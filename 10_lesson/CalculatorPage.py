from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    def __init__(self, driver):
        """
        Конструктор класса CalculatorPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы калькулятора")
    def get(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    @allure.step("Установка задержки 45 секунд")
    def calc_wait(self):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        """
        self.driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    @allure.step("Нажатие кнопок: 7, +, 8, =")
    def button_calc(self):
        """
        Нажимает на кнопки калькулятора для подтверждения работы
        """

        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Получение результата с экрана калькулятора")
    def result_field(self):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        """
        WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element((
             By.CLASS_NAME, "screen"), "15"))
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        """
        Возвращает текущий результат с экрана калькулятора.
        :return: str — текст результата на экране калькулятора.
        """
        return result
