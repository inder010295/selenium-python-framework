from selenium.webdriver.common.by import By

from Selenium_Project.Utilities.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        username = (By.ID,"user-name")
        password = (By.ID,"password")
        submit_btn = (By.ID,"login-button")

    def login(self, user, pwd):
        self.type(self.username,user)
        self.type(self.password,pwd)
        self.click(self.submit_btn)


