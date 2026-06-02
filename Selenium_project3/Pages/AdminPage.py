from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Selenium_project3.Utilities.basepage import basepage


class AdminPage(basepage):
    def __init__(self,driver):
        super().__init__(driver)

    username_input = (By.XPATH, "//label[text()='Username']/following::input[1]")

    dropdown = (By.XPATH, "//div[contains(@class,'oxd-select-text')]")
    option = (By.XPATH, "//div[@role='option'][1]")

    dropdown1 = (By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][4]")
    option1 = (By.XPATH, "//div[@role='option'][1]")

    submit = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.type(self.username_input, username)


    def drop_down(self):
        self.click(self.dropdown)
        self.click(self.option)

    def drop_down1(self):
        self.click(self.dropdown1)
        self.click(self.option1)

    def submit_btn(self):
        self.click(self.submit)
