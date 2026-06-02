from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium_Project.Utilities.BasePage import BasePage

class CartPage(BasePage):

    def verify_cart_page(self):
        title = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        ).text
        assert "cart" in title.lower()

    def get_cart_items_count(self):
        items = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )
        return len(items)

    def click_checkout(self):
        checkout_btn = self.wait.until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        # 🔥 FORCE CLICK
        self.driver.execute_script("arguments[0].click();", checkout_btn)
