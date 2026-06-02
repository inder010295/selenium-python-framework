from Selenium_Project5.Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AccountCreated(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    success_heading = (By.XPATH, "//h1[contains(text(),'Account Opened')]")
    new_account_number = (By.XPATH,"//b[contains(text(),'Your new account number')]/following-sibling::a")
    Tr_fund = (By.XPATH,"//a[contains(text(), 'Transfer Funds')]")


    def verify_account_opened(self):
        heading_text = self.wait.until(EC.visibility_of_element_located(self.success_heading)).text

        print("Success Heading:", heading_text)
        assert "Account Opened" in heading_text

    def get_new_account_number(self):
        acc_no = self.wait.until(EC.visibility_of_element_located(self.new_account_number)).text
        print("My New Opened Account Number is:", acc_no)
        return acc_no


    def click_transfer_fund(self):
        self.click(self.Tr_fund)

