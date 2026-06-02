from Selenium_project3.Utilities.basepage import basepage
from selenium.webdriver.common.by import By


class LoginPage(basepage):
    def __init__(self,driver):
        super().__init__(driver)

    username = (By.NAME,"username")
    password = (By.NAME,"password")
    login_btn = (By.XPATH,"//button[@type='submit']")

    def login(self,user,pwd):
        self.type(self.username,user)
        self.type(self.password,pwd)
        self.click(self.login_btn)



