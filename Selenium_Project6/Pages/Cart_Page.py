from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_Project6.Utilities.BasePage import BasePage


class Cart_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    cart_btn = (By.XPATH,"//a[contains(text(),'Cart')]")
    place_order_btn = (By.XPATH,"//button[contains(text(),'Place Order')]")

    po_name = (By.ID,"name")
    po_country = (By.ID,"country")
    po_city = (By.ID,"city")
    po_credit_card =(By.ID,"card")
    po_month = (By.ID,"month")
    po_year = (By.ID,"year")
    purchase_btn = (By.XPATH,"//button[contains(text(),'Purchase')]")

    alert_msg = (By.XPATH,"//h2[contains(text(),'Thank you for your purchase!')]")
    order_details = (By.XPATH,"//p[contains(@class,'lead text-muted')]")
    order_confirm = (By.XPATH,"//button[contains(text(),'OK')]")

    def click_cart_and_place_order(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.place_order_btn)).click()

    def place_order_info(self,name,country,city,credit_card,month,year):
        self.wait.until(EC.visibility_of_element_located(self.po_name)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.po_country)).send_keys(country)
        self.wait.until(EC.visibility_of_element_located(self.po_city)).send_keys(city)
        self.wait.until(EC.visibility_of_element_located(self.po_credit_card)).send_keys(credit_card)
        self.wait.until(EC.visibility_of_element_located(self.po_month)).send_keys(month)
        self.wait.until(EC.visibility_of_element_located(self.po_year)).send_keys(year)
        self.wait.until(EC.element_to_be_clickable(self.purchase_btn)).click()

    def order_validation(self):
        order_msg = self.wait.until(EC.visibility_of_element_located(self.alert_msg))
        print("Order Message:", order_msg.text)
        self.take_screenshot("order_confirmation")

        details = self.wait.until(EC.visibility_of_element_located(self.order_details))
        print("Order Details:\n", details.text)
        assert "Thank you for your purchase!" in order_msg.text
        self.wait.until(EC.element_to_be_clickable(self.order_confirm)).click()




