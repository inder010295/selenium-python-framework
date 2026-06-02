from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium_Project.Utilities.BasePage import BasePage
import time


class CheckoutPage(BasePage):

    def verify_checkout_page(self):
        self.wait.until(EC.url_contains("checkout-step-one.html"))
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

    def fill_checkout_information(self, first, last, zip_code):

        fn = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        fn.click()
        fn.clear()
        fn.send_keys(first)

        ln = self.wait.until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        )
        ln.click()
        ln.clear()
        ln.send_keys(last)

        pc = self.wait.until(
            EC.visibility_of_element_located((By.ID, "postal-code"))
        )
        pc.click()
        pc.clear()
        pc.send_keys(zip_code)

        # 🔥 HARD PROOF (remove later)
        time.sleep(1)
        print("FN:", fn.get_attribute("value"))
        print("LN:", ln.get_attribute("value"))
        print("PC:", pc.get_attribute("value"))

        # ✅ ONLY NORMAL CLICK
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

    def verify_overview_page(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))

    def click_finish(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        ).click()
