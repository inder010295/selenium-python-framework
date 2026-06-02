from Selenium_Project6.Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    Login_btn = (By.ID,"login2")
    Login_username = (By.ID, "loginusername")
    Login_password = (By.ID, "loginpassword")
    SignIn_btn = (By.XPATH, "//button[contains(text(),'Log in')]")

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.Login_btn)).click()

    def fill_info_login(self,username,password):
        self.wait.until(EC.visibility_of_element_located(self.Login_username)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.Login_password)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.SignIn_btn)).click()

    def logged_in(self):
        text = self.driver.title
        print("Logged In Message", text)
        self.take_screenshot("login_success")

