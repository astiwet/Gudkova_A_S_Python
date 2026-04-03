from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.implicitly_wait(20) 

driver.get("https://uitestingplayground.com/textinput")

element = driver.find_element(By.ID, "newButtonName")
element.send_keys("Skypro")

driver.find_element(By.CLASS_NAME, "btn-primary").click()

Name = driver.find_element(By.CLASS_NAME, "btn-primary")

print(f"{Name.text}")

driver.quit()










#print(element)

driver.quit()