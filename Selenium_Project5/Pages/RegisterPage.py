from selenium.webdriver.common.by import By

from Selenium_Project5.Utilities.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    register_click_btn = (By.XPATH,"//a[contains(text(),'Register')]")

    def click_register(self):
        self.click(self.register_click_btn)

    def verify_register_page(self):
        title = self.driver.title
        assert "ParaBank | Register for Free Online Account Access" in title
        print("Register Page Title: ",title)