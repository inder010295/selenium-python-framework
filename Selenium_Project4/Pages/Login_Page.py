from selenium.webdriver.common.by import By
from Selenium_Project4.Utilities.Base_Page import BasePage

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.ID, "submit")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()