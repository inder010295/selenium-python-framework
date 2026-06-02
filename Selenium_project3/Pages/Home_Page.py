from Selenium_project3.Utilities.basepage import basepage
from selenium.webdriver.common.by import By

from Selenium_project3.conftest import driver


class HomePage(basepage):
    def __init__(self,driver):
        super().__init__(driver)

        self.admin_btn_click = (By.XPATH,"//span[normalize-space()='Admin']")

    def go_to_admin_page(self):
        self.click(self.admin_btn_click)


