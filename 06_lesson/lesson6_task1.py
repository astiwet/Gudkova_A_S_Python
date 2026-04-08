from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://www.uitestingplayground.com/ajax")

button = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#ajaxButton")))
button.click()

content = driver.find_element(By.CSS_SELECTOR, "#content")

wait = WebDriverWait(driver, 20)
message = wait.until(EC. visibility_of_element_located((By.CSS_SELECTOR,"p.bg-success")))

print(message.text)

driver.quit()