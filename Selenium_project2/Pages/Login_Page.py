from selenium.webdriver.common.by import By

from Selenium_project2.Utilities.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "submit")

    def login(self, user, pwd):
        self.type(self.username,user)
        self.type(self.password,pwd)
        self.click(self.login_btn)