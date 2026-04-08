import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.edge.service import Service

from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture

def driver():

    edge_driver_path = r"C:\Users\puhlo\OneDrive\Desktop\edge\msedgedriver.exe"

    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    driver.maximize_window()

    yield driver

    driver.quit()



def test_form(driver):

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 30)

    wait.until(EC.presence_of_element_located((By.ID, 'First name')))

 

    driver.find_element(By.ID, "First name").send_keys("Иван") 

    driver.find_element(By.ID, "Last name").send_keys("Петров")

    driver.find_element(By.ID, "Address").send_keys("Ленина, 55-3")

    driver.find_element(By.ID, "E-mail").send_keys("test@skypro.com")

    driver.find_element(By.ID, "Phone number").send_keys("+7985899998787")

    driver.find_element(By.ID, "Zip code").send_keys("")

    driver.find_element(By.ID, "City").send_keys("Москва")

    driver.find_element(By.ID, "Country").send_keys("Россия")

    driver.find_element(By.ID, "Job position").send_keys("QA")

    driver.find_element(By.ID, "Company").send_keys("SkyPro")



    # Нажимаем кнопку Submit  

    driver.find_element(By.ID, "submit").click()



    # Ждем, пока форма обработается  

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "form-group")))



    # Проверяем, что Zip code подсвечен красным  

    zip_code_field = driver.find_element(By.ID, "zip-code")

    assert "border-color: red" in zip_code_field.get_attribute("style"), "Zip code field is not highlighted in red."



    # Проверяем, что остальные поля подсвечены зеленым  

    fields = [

        "first-name",

        "last-name",

        "address",

        "e-mail",

        "phone",

        "city",

        "country",

        "job position",

        "company"

    ]



    for field_name in fields:

        field = driver.find_element(By.ID, field_name)

        assert "border-color: green" in field.get_attribute("style"), f"{field_name} field is not highlighted in green."



     # Закрываем драйвер  

    driver.quit()