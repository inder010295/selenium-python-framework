from Selenium_project3.Pages.AdminPage import AdminPage
from Selenium_project3.Pages.Home_Page import HomePage
from Selenium_project3.Pages.loginpage import LoginPage
import sys
print(sys.path)

def test_login(driver):
    login = LoginPage(driver)
    login.login("Admin", "admin123")


    home = HomePage(driver)
    home.go_to_admin_page()

    admin = AdminPage(driver)
    admin.enter_username("Brody_DAmore57")
    admin.drop_down()
    admin.drop_down1()
    admin.submit_btn()
