import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from Simple_Python_Project.Utilities.base_page import BasePage


class HomePage(BasePage):

    # Locators
    name_input     = (By.ID, "name")
    email_input    = (By.ID, "email")
    phone_input    = (By.ID, "phone")
    address_input  = (By.ID, "textarea")
    radio_input    = (By.ID, "male")
    checkbox_input = (By.ID, "tuesday")

    country_dd = (By.ID, "country")
    colors_dd  = (By.ID, "colors")
    animals_dd = (By.ID, "animals")

    date_picker1 = (By.ID, "datepicker")
    date_picker2 = (By.ID, "txtDate")
    start_date   = (By.ID, "start-date")
    end_date     = (By.ID, "end-date")

    submit_btn = (By.XPATH, "//button[contains(@class,'submit-btn')]")

    alert = (By.ID,"alertBtn")
    conf_alert = (By.ID,"confirmBtn")
    prompt_alert_btn = (By.ID,"promptBtn")

    new_tab = (By.XPATH,"//button[normalize-space()='New Tab']")
    pop_window = (By.ID,"PopUp")

    point_me = (By.CLASS_NAME,"dropbtn")
    sub_menu1 =(By.XPATH,"//div[@class='dropdown-content']/a[1]")
    sub_menu2 = (By.XPATH,"//div[@class='dropdown-content']/a[2]")

    field1 = (By.ID,"field1")
    field2 = (By.ID,"field2")
    copy_btn = (By.XPATH,"//button[normalize-space()='Copy Text']")

    drag_source = (By.ID,"draggable")
    drag_target = (By.ID,"droppable")


    # Actions
    def enter_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.name_input)).send_keys(name)

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)

    def enter_phone(self, phone):
        self.wait.until(EC.visibility_of_element_located(self.phone_input)).send_keys(phone)

    def enter_address(self, address):
        self.wait.until(EC.visibility_of_element_located(self.address_input)).send_keys(address)

    def select_radio(self):
        self.click(self.radio_input)

    def select_checkbox(self):
        self.click(self.checkbox_input)

    def select_dropdown(self, locator, value):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        Select(element).select_by_visible_text(value)

    def color_list(self, value):
        element = self.wait.until(
            EC.presence_of_element_located(self.colors_dd)
        )
        select = Select(element)
        select.select_by_visible_text(value)

    def animals_list(self,locator):
        self.click(self.animals_dd)

    def set_date(self, locator, date):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(date)

    def submit(self):
        self.click(self.submit_btn)

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def click_alert_btn(self):
        self.scroll_to_top()
        self.click(self.alert)
        alert = self.wait.until(EC.alert_is_present())
        alert_txt = alert.text
        print("Alert Text: ", alert_txt)
        alert.accept()
        return alert_txt

    def click_conf_alert_btn(self):
        self.click(self.alert)
        alert = self.wait.until(EC.alert_is_present())
        confirm_text = alert.text
        print("Confirm_Alert Text: ", confirm_text)
        alert.accept()

    def click_prompt_alert(self, value):
        self.click(self.prompt_alert_btn)
        alert = self.wait.until(EC.alert_is_present())
        print("Prompt Message:", alert.text)
        alert.send_keys(value)
        alert.accept()
        print("Entered Value:", value)
        return value

    def click_new_tab(self):
        parent_window = self.driver.current_window_handle
        self.click(self.new_tab)

        all_windows =self.driver.window_handles
        for window in all_windows:
            if window != parent_window:
                self.driver.switch_to.window(window)
                break

        print("Opened New tab", self.driver.title)
        assert "SDET-QA Blog" in self.driver.title

        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def click_popup_window(self):
        parent_window = self.driver.current_window_handle
        self.click(self.pop_window)
        self.wait.until(lambda d: len(d.window_handles) > 2)

        all_windows =self.driver.window_handles
        for window in all_windows:
            if window != parent_window:
                self.driver.switch_to.window(window)
                break

        if "Playwright" in self.driver.title:
            print("Popup window found:", self.driver.title)
            self.driver.close()

        elif "SDET-QA Blog" in self.driver.title:
            print("Blog tab found:", self.driver.title)
            self.driver.close()

        self.driver.switch_to.window(parent_window)

    def hover_and_click_submenu(self, main_menu, sub_menu):
        main = self.wait.until(EC.visibility_of_element_located(main_menu))

        ActionChains(self.driver).move_to_element(main).click().perform()

        sub = self.wait.until(EC.visibility_of_element_located(sub_menu))
        sub.click()

    def field_input(self, text):
        field1 = self.wait.until(EC.visibility_of_element_located(self.field1))
        field1.clear()  # 🔥 MOST IMPORTANT LINE
        field1.send_keys(text)

    def double_click(self):
        copy_btn = self.wait.until(EC.element_to_be_clickable(self.copy_btn))
        ActionChains(self.driver).double_click(copy_btn).perform()

    def get_field2_text(self):
        field2 = self.wait.until(EC.visibility_of_element_located(self.field2))
        return field2.get_attribute("value")


    def drag_and_drop(self):
        source = self.wait.until(EC.visibility_of_element_located(self.drag_source))
        target = self.wait.until(EC.visibility_of_element_located(self.drag_target))
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def get_drop_text(self):
        target = self.wait.until(EC.visibility_of_element_located(self.drag_target))
        return target.text









