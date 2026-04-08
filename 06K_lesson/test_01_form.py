import pytest

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_form(driver):
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 30).until(EC. visibility_of_element_located((By.NAME, "first-name"))).send_keys("Иван")

    driver.find_element(By.NAME, "last-name").send_keys("Петров")

    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина,55-3")

    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    p_number = driver.find_element(By.NAME, "phone")
    p_number.send_keys("+7985899998787")

    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job_p = driver.find_element(By.NAME, "job-position")
    job_p.send_keys("QA")

    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    wait = WebDriverWait(driver, 15)
    button = wait.until(EC. visibility_of_element_located((By.TAG_NAME,"button")))
    button.click()

    fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company"]

    for field in fields:
        field_color = driver.find_element(By.ID, field).value_of_css_property("background-color")
        assert field_color == "rgba(209, 231, 221, 1)"

        #field = driver.find_element(By.ID, field)
        #assert "success" in field.get_attribute("class")

    zip_code_color = driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")
    assert zip_code_color == "rgba(248, 215, 218, 1)"

    #zip_code = driver.find_element(By.ID, "zip-code")
    #assert "danger" in zip_code.get_attribute("class")

    driver.quit()



#zip_code_color = driver.find_element(By.ID, "zip-code").value_of_css_property("background-color")
#assert zip_code_color == "rgba(248, 215, 218, 1)", "Поле Zip code должно быть подсвечено красным"