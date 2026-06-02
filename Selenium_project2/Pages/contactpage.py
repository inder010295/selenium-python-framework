import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium_project2.Utilities.BasePage import BasePage


class Contact_page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # 🔹 LOCATORS (ALL MUST BE self.)
        self.f_name_input = (By.ID, "wpforms-161-field_0")
        self.l_name_input = (By.ID, "wpforms-161-field_0-last")
        self.email_input = (By.ID, "wpforms-161-field_1")
        self.comment_input = (By.ID, "wpforms-161-field_2")
        self.submit_btn = (By.ID, "wpforms-submit-161")

    def verify_contact_page(self):
        self.wait.until(EC.title_contains("Contact"))

    def fill_information_form(self, first_name, last_name, email, comment):
        self.type(self.f_name_input, first_name)
        self.type(self.l_name_input, last_name)
        self.type(self.email_input, email)
        self.type(self.comment_input, comment)

    def wait_for_captcha_manual(self):
        print("🧠 Solve CAPTCHA manually (10 seconds)...")
        time.sleep(10)

    def submit_contact_form(self):
        self.click(self.submit_btn)
