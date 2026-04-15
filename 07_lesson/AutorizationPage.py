

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutorizationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
       

    def open(self):
        self.driver.get("https://www.saucedemo.com/")


    def autorization_login(self, term):
        self.driver.find_element(By.ID, "user-name").send_keys(term)

    def autorization_pass(self, term):
        self.driver.find_element(By.ID, "password").send_keys(term)
            

    def login_button(self):
        self.wait.until(EC. element_to_be_clickable((By.ID, "login-button"))).click()