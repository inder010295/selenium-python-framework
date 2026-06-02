from click import option
from selenium.webdriver.support.select import Select

from Selenium_Project5.Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OpenAccHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    dropdown_locator = (By.ID, "type")
    amount_locator = (By.ID, "fromAccountId")
    Open_new_account_btn = (By.XPATH, "//input[@value ='Open New Account']")

    def select_account_type(self, account_type):
        dropdown_element = self.wait.until(EC.presence_of_element_located(self.dropdown_locator))
        Select(dropdown_element).select_by_visible_text(account_type)
        print("Select Account Type: ", account_type)

    def print_account_amount(self):
        dropdown = self.wait.until(
            EC.presence_of_element_located(self.amount_locator)
        )

        select = Select(dropdown)

        # 🔥 WAIT until options are populated
        WebDriverWait(self.driver, 10).until(
            lambda d: len(select.options) > 0
        )

        first_account = select.options[0].text
        select.select_by_visible_text(first_account)

        print("Selected Account Amount:", first_account)
        return first_account

    def click_open_account_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.Open_new_account_btn)).click()



