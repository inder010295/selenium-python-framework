from Selenium_Project5.Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransferFund(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    transfer_amount = (By.ID,"amount")
    transfer_btn = (By.XPATH,"//input[@type='submit']")

    def trans_amount(self,value):
        self.wait.until(EC.element_to_be_clickable(self.transfer_amount)).send_keys(value)

    def click_trans_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.transfer_btn)).click()
        print("Transfer Button Click Successfully")


