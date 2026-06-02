from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


from Automation_Practise.Utilities.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

        self.name = (By.ID,'name')
        self.email = (By.ID,'email')
        self.phone = (By.ID,'phone')
        self.Address = (By.ID,'textarea')
        self.Gender = (By.ID,'male')
        self.Days = (By.ID,'sunday')
        self.Country = (By.ID,'country')
        self.Colors = (By.ID,'colors')
        self.Sorted_list = (By.ID,'animals')
        self.Date_Picker1 = (By.ID,'datepicker')
        self.Date_Picker2 = (By.ID,'txtDate')
        self.Date_Picker3 = (By.ID,'start-date')
        self.Date_Picker4 = (By.ID,'end-date')
        self.Submit = (By.XPATH,'//button[@class ="submit-btn"]')


    def enter_name(self, name):
            self.wait.until(EC.visibility_of_element_located(self.name)).send_keys(name)

    def enter_email(self, email):
            self.wait.until(EC.visibility_of_element_located(self.email)).send_keys(email)

    def enter_phone(self, phone):
            self.wait.until(EC.visibility_of_element_located(self.phone)).send_keys(phone)

    def enter_address(self, address):
            self.wait.until(EC.visibility_of_element_located(self.Address)).send_keys(address)

    def select_radio(self):
            self.click(self.Gender)

    def select_checkbox(self):
            self.click(self.Days)

    def select_dropdown(self,locator,value):
            element =self.wait.until(EC.element_to_be_clickable(locator))
            Select(element).select_by_value(value)

    def color_list(self,value):
            element = self.wait.until(EC.presence_of_element_located(self.Colors))
            Select(element).select_by_visible_text(value)

    def animals_list(self,locator):
        self.click(self.Sorted_list)

    def set_date(self, locator, date):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(date)

    def submit(self):
        self.click(self.Submit)




