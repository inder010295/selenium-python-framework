from Selenium_Project4.Utilities.Base_Page import BasePage
from selenium.webdriver.common.by import By


class pre_homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    home_click_button = (By.XPATH,"//a[normalize-space()='Home']")


    def verify_prehompage(self):
        assert "Logged In Successfully" in self.driver.title

    def go_to_homepage(self):
        self.click(self.home_click_button)
