import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работу калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """
    Тест проверяет работу калькулятора.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    calculator_page = CalculatorPage(driver)
    calculator_page.get()
    calculator_page.calc_wait()
    calculator_page.button_calc()
    result = calculator_page.result_field()
    with allure.step("Проверка результата"):
        assert result == '15'
