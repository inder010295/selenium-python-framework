import driver

from Selenium_Project5.Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By



class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    f_name_input = (By.ID,"customer.firstName")
    l_name_input = (By.ID,"customer.lastName")
    address_input = (By.ID,"customer.address.street")
    city_input = (By.ID,"customer.address.city")
    state_input = (By.ID,"customer.address.state")
    zip_input = (By.ID,"customer.address.zipCode")
    phone_input = (By.ID,"customer.phoneNumber")
    ssn_input = (By.ID,"customer.ssn")

    username_input = (By.ID,"customer.username")
    password_input = (By.ID,"customer.password")
    confirm_password_input = (By.ID,"repeatedPassword")

    Register_btn = (By.XPATH,"//input[@value='Register']")

    def basic_details (self,first_name, last_name, address, city, state, zip_code, phone, ssn, username, password,confirm_password):
        self.type(self.f_name_input, first_name)
        self.type(self.l_name_input, last_name)
        self.type(self.address_input, address)
        self.type(self.city_input, city)
        self.type(self.state_input, state)
        self.type(self.zip_input, zip_code)
        self.type(self.phone_input, phone)
        self.type(self.ssn_input, ssn)
        self.type(self.username_input, username)
        self.type(self.password_input, password)
        self.type(self.confirm_password_input, password)

    def register_btn(self):
        self.click(self.Register_btn)

    def register_successfully(self):
        title = self.driver.title
        assert "ParaBank | Customer Created" in title
        print("User Registered Sucessfully", self.driver.title)



