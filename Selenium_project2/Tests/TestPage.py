from Selenium_project2.Pages.Login_Page import LoginPage
from Selenium_project2.Pages.contactpage import Contact_page
from Selenium_project2.Pages.homepage import HomePage


def test_login(driver):
    login = LoginPage(driver)
    login.login("student","Password123")

    home = HomePage(driver)
    home.verify_homepage()


    home.go_to_contact_page()

    contact = Contact_page(driver)
    contact.verify_contact_page()
    contact.fill_information_form("inder","singh","inderbhai@gmail.com","Hello Sir! How are you?")
    contact.wait_for_captcha_manual()
    contact.submit_contact_form()






