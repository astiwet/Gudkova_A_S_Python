import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    user = driver.find_element(By.ID,"user-name")
    user.send_keys("standard_user")

    password = driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    
    WebDriverWait(driver, 10).until(EC. visibility_of_element_located((By.ID,"login-button"))).click()

    WebDriverWait(driver, 10).until(EC. visibility_of_element_located((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack"))).click()

    WebDriverWait(driver, 10).until(EC. visibility_of_element_located((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-bolt-t-shirt"))).click()

    WebDriverWait(driver, 10).until(EC. visibility_of_element_located((By.CSS_SELECTOR,"#add-to-cart-sauce-labs-onesie"))).click()
     
    WebDriverWait(driver, 10).until(EC. visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link"))).click()

    #WebDriverWait(driver, 10).until(EC. visibility_of_element_located((By.CLASS_NAME,"title")))

    WebDriverWait(driver, 10).until(EC. visibility_of_element_located((By.ID,"checkout"))).click()

    f_name = driver.find_element(By.ID, "first-name")
    f_name.send_keys("Иван")

    l_name = driver.find_element(By.ID, "last-name")
    l_name.send_keys("Петров")

    post_code = driver.find_element(By.ID, "postal-code")
    post_code.send_keys("12345678")

    WebDriverWait(driver, 30).until(EC. visibility_of_element_located((By.ID,"continue"))).click()
    
   # WebDriverWait(driver, 15).until(EC. visibility_of_element_located((By.CLASS_NAME,"#Overview")))

    total = WebDriverWait(driver, 15).until(EC. visibility_of_element_located((By.CLASS_NAME,"summary_total_label")))
    total_price = total.text
    assert total_price == "Total: $58.29"

    driver.quit()





    


