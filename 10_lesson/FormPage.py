
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class FormPage:
    def __init__(self, driver):
        """
        Конструктор класса FormPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        """
        Поля для заполнения формы даннымы пользователя
        """
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открытие страницы для заполнения формы")
    def open(self):
        """
        Открывает страницу формы.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )

    @allure.step("Заполнение полей формы данными пользователя")
    def fill_form(self):
        """
        Заполняет поля формы.
        :param value: str — данные для заполнения полей формы.
        """
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажатие на кнопку Submit для просмотра заполненной формы")
    def submit_form(self):
        """
        Нажимает на кнопку Submit по окончании заполнения формы.
        """
        self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Получение класса элемента {field_id}")
    def get_field_class(self, field_id):
        """
        Получает атрибут элемента
        :param field_id: str — наименование класса.
        """
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        """
        Возвращает аттрибут элемента
        :return element: str — наименование класса
        """
        return element

    @allure.step("Тест на проверку,что поле Zip code подсвечено красным")
    def check_zip_code_error(self):
        """
        Возвращает элемент из метода получения класса
        :return: str — наименование класса
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Тест на проверку, что остальные поля подсвечены зеленым. ")
    def check_fields_success(self):
        """
        Проверяет заполнение всех полей, кроме поля zip-code
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверка заполнения формы")
    def check_form_submission(self):
        """
        Проверяет, что поле Zip code подсвечено красным.
        """
        assert self.check_zip_code_error()
        """
        Проверяет, что остальные поля подсвечены зеленым.
        """
        assert self.check_fields_success()
