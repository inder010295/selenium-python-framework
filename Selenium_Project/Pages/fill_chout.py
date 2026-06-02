from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def fill_checkout_information(self, first, last, zip_code):

    # FIRST NAME
    fn = self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    fn.click()
    time.sleep(0.3)
    self.driver.switch_to.active_element().send_keys(Keys.CONTROL, "a")
    self.driver.switch_to.active_element().send_keys(Keys.DELETE)
    self.driver.switch_to.active_element().send_keys(first)

    # LAST NAME
    ln = self.wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
    ln.click()
    time.sleep(0.3)
    self.driver.switch_to.active_element().send_keys(Keys.CONTROL, "a")
    self.driver.switch_to.active_element().send_keys(Keys.DELETE)
    self.driver.switch_to.active_element().send_keys(last)

    # ZIP CODE
    pc = self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
    pc.click()
    time.sleep(0.3)
    self.driver.switch_to.active_element().send_keys(Keys.CONTROL, "a")
    self.driver.switch_to.active_element().send_keys(Keys.DELETE)
    self.driver.switch_to.active_element().send_keys(zip_code)

    # CONTINUE (NORMAL CLICK ONLY)
    self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
