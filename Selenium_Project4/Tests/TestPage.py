import pytest

from Selenium_Project4.Pages.Login_Page import LoginPage
from Selenium_Project4.Pages.Prehomepage import pre_homepage
from Selenium_Project4.Pages.Home_Page import Homepage

@pytest.mark.usefixtures("driver")
class TestFlow:

    def test_validation(self):
        login = LoginPage(self.driver)
        login.login("student", "Password123")


    def test_homepage(self):
        pre_home = pre_homepage(self.driver)
        pre_home.verify_prehompage()
        pre_home.go_to_homepage()

    def test_homepage2(self):
        home = Homepage(self.driver)
        home.verify_homepage()
        home.click_button()


