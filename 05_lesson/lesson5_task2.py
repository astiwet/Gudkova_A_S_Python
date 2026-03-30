from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

wait = WebDriverWait(driver, 5)
button = wait.until(EC. visibility_of_element_located((By.TAG_NAME,"button")))
button.click()

wait = WebDriverWait(driver, 5)
button = wait.until(EC. visibility_of_element_located((By.TAG_NAME,"button")))
button.click()

wait = WebDriverWait(driver, 5)
button = wait.until(EC. visibility_of_element_located((By.TAG_NAME,"button")))
button.click()


sleep(10)