from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)
name_imput = driver.find_element(By.ID, "username")
name_imput.send_keys("tomsmith")

pass_imput = driver.find_element(By.ID, "password")
pass_imput.send_keys("SuperSecretPassword!")

login_imput = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_imput.click()

wait = WebDriverWait(driver, 15)
message = wait.until(EC. visibility_of_element_located((By.CSS_SELECTOR,"div.flash" )))

print(message.text)

driver.quit()