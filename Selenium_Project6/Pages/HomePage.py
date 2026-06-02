from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_Project6.Utilities.BasePage import BasePage

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    sony_xperia = (By.XPATH,"//a[contains(text(),'Sony xperia z5')]")
    sony_vio = (By.XPATH,"//a[contains(text(),'Sony vaio i7')]")
    nokia_lumia_1520 = (By.XPATH,"//a[contains(text(),'Nokia lumia 1520')]")

    add_to_cart = (By.XPATH,"//a[contains(text(),'Add to cart')]")
    home_btn = (By.XPATH,"//a[contains(text(),'Home')]")

    def click_mobiles(self):
        self.wait.until(EC.element_to_be_clickable(self.sony_xperia)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart)).click()
        print("Sony xperia Page", self.driver.title)
        alert = WebDriverWait(self.driver,10).until(EC.alert_is_present())
        text = alert.text
        print("Alert Message", text)
        alert.accept()
        self.driver.back()

        self.wait.until(EC.element_to_be_clickable(self.home_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.sony_vio)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart)).click()
        print("Sony Vio", self.driver.title)
        alert = WebDriverWait(self.driver,10).until(EC.alert_is_present())
        text = alert.text
        print("Alert Message", text)
        alert.accept()
        self.driver.back()

        self.wait.until(EC.element_to_be_clickable(self.home_btn)).click()
        self.wait.until(EC.element_to_be_clickable(self.nokia_lumia_1520)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart)).click()
        print("Nokia Lumia", self.driver.title)
        alert = WebDriverWait(self.driver,10).until(EC.alert_is_present())
        text = alert.text
        print("Alert Message", text)
        alert.accept()
        self.driver.back()






