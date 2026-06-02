import os
import time
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def type(self,locator,value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def take_screenshot(self,name):
        folder = "Screenshot"

        if not os.path.exists(folder):
            os.makedirs(folder)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            file_path = f"{folder}/{name}_{timestamp}.png"
            self.driver.save_screenshot(file_path)
            print("Screenshot saved:", file_path)



