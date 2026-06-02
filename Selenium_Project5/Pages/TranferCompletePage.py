from Selenium_Project5.Utilities.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class TransferCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    heading = (By.XPATH,"//h1[contains(text(),'Transfer Complete!')]")
    Message = (By.ID, "showResult")

    def verify_transfer_heading(self):
        heading_text = self.wait.until(EC.visibility_of_element_located(self.heading)).text
        print("Heading",heading_text)
        assert "Transfer Complete!" in heading_text

    def verify_transfer_message(self):
        mesage_text = self.wait.until(EC.visibility_of_element_located(self.Message)).text
        print("Message",mesage_text)
        return



