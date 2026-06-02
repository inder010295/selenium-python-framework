from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Selenium_project2.conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def type(self, locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()
