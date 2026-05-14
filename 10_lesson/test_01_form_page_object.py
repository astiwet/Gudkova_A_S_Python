import pytest
from selenium import webdriver
from FormPage import FormPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Edge()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование заполнения формы")
@allure.description("Тест проверяет корректность заполнения формы")
@allure.feature("Форма")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    """
    Тест проверяет правильность заполнения формы

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()
