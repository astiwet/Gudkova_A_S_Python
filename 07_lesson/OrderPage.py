
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrgerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'firstName': "Иван",
            'lastName': "Петров",
            'postalCode': "123456"
        }

    def user_info(self):
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)
    
    def making_order(self):
        self.wait.until(
        EC. visibility_of_element_located((By.ID, "continue"))).click()

    def total_price(self):
        total = self.wait.until(EC. visibility_of_element_located((
            By.CLASS_NAME, "summary_total_label"))).text
        total_str = total.split()[-1]
        return total_str
