from Selenium_Project5.Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By


class OpenAccPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    click_open_account_btn = (By.XPATH,"//a[contains(text(),'Open New Account')]")

    def click_open_account(self):
        self.click(self.click_open_account_btn)

    def verify_open_account(self):
        title = self.driver.title
        assert "ParaBank | Open Account" in title
        print("Open New Account", self.driver.title)