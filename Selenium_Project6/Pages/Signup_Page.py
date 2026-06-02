from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_Project6.Utilities.BasePage import BasePage


class Signup_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    signup_btn = (By.ID,"signin2")
    Sign_username = (By.ID,"sign-username")
    Sign_password = (By.ID,"sign-password")
    Sign_Register = (By.XPATH,"//button[contains(text(),'Sign up')]")

    def click_signup(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_btn)).click()

    def fill_info_signup(self,username,password):
        self.wait.until(EC.visibility_of_element_located(self.Sign_username)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.Sign_password)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.Sign_Register)).click()

    def regi_val(self):
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        print("Alert Message",alert.text)
        alert.accept()
        self.take_screenshot("signup_success")


