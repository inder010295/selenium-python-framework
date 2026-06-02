from Selenium_Project.Pages.Home_Page import HomePage
from Selenium_Project.Pages.LoginPage import LoginPage
from Selenium_Project.Pages.cart_page import CartPage
from Selenium_Project.Pages.checkout_page import CheckoutPage


def test_valid_page(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    home = HomePage(driver)
    home.all_add_to_cart_button()
    home.go_to_cart()

    cart = CartPage(driver)
    cart.verify_cart_page()
    assert cart.get_cart_items_count() > 0
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.verify_checkout_page()
    checkout.fill_checkout_information("Inder", "Singh", "250001")

    checkout.verify_overview_page()
    checkout.click_finish()
