from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Selenium_Project.Utilities.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def all_add_to_cart_button(self):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.add_to_cart_buttons)
        )

        for btn in buttons:
            if btn.text.strip().lower() == "add to cart":
                btn.click()

    def go_to_cart(self):
        # 🔥 JS click to FORCE navigation
        cart = self.wait.until(
            EC.presence_of_element_located(self.cart_icon)
        )
        self.driver.execute_script("arguments[0].click();", cart)

