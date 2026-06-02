from Selenium_Project4.Utilities.Base_Page import BasePage
from selenium.webdriver.common.by import By

class Homepage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    name_input = (By.ID,"form_first_name_7")
    email_input = (By.ID,"form_email_7")
    get_path = (By.CLASS_NAME,"mailpoet_submit")

    def verify_homepage(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def click_button(self):
        self.click(self.get_path)

