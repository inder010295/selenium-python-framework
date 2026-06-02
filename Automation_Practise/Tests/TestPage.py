from Simple_Python_Project.Pages.home_page import HomePage
from selenium.webdriver.common.by import By


def test_page_validation(driver):


    home = HomePage(driver)
    home.enter_name("Inderpal Singh")
    home.enter_email("inder010295@gmail.com")
    home.enter_phone("975637383")
    home.enter_address("Gaur City2, Greater Noida West")

    home.select_radio()
    home.select_checkbox()

    home.select_dropdown(home.country_dd, "India")
    home.color_list("Red")
    home.animals_list("dog")

    home.set_date(home.date_picker1, "02/01/1994")
    home.set_date(home.date_picker2, "02/05/1994")
    home.set_date(home.start_date, "02/10/2024")
    home.set_date(home.end_date, "02/15/2024")

    home.submit()