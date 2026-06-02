import sys
import time
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Selenium_Project6.Pages.Cart_Page import Cart_Page
from Selenium_Project6.Pages.HomePage import HomePage
from Selenium_Project6.Pages.Login_Page import Login_Page
from Selenium_Project6.Pages.Signup_Page import Signup_Page

@pytest.mark.smoke
def test_valid(driver):
    signup = Signup_Page(driver)
    signup.click_signup()
    signup.fill_info_signup("Inder511","Adobe@123")
    signup.regi_val()

@pytest.mark.smoke
def test_login(driver):
    login = Login_Page(driver)
    login.click_login()
    login.fill_info_login("Inder511","Adobe@123")
    login.logged_in()

    time.sleep(10)

@pytest.mark.regression
def test_home_page(driver):
    home = HomePage(driver)
    home.click_mobiles()

@pytest.mark.regression
def test_cart_page(driver):
    cart = Cart_Page(driver)
    cart.click_cart_and_place_order()
    cart.place_order_info("inder","india","Meerut","4567576786859876","March","2026")
    cart.order_validation()


