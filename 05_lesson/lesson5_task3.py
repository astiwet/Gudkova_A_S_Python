from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/inputs")
sleep(5)

search_locator = "input"
search_imput = driver.find_element(By.TAG_NAME, search_locator)
search_imput.send_keys("12345")

sleep(5)

search_imput.clear()

search_imput = driver.find_element(By.TAG_NAME, search_locator)
search_imput.send_keys("54321")

sleep(5)

driver.quit()