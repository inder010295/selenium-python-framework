from Selenium_project2.Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.contact_link = (By.XPATH,"//a[normalize-space()='Contact']")


    def verify_homepage(self):
        assert "Logged In Successfully | Practice Test Automation" in self.driver.title


    def go_to_contact_page(self):
        self.click(self.contact_link)


