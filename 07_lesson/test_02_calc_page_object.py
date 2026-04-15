import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.get()
    calculator_page.calc_wait()
    calculator_page.button_calc()
    result = calculator_page.result_field()
    assert result == '15'
