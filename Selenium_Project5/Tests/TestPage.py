import time

from Selenium_Project5.Pages.AccountCreated import AccountCreated
from Selenium_Project5.Pages.HomePage import HomePage
from Selenium_Project5.Pages.OpenAccountHomePage import OpenAccHomePage
from Selenium_Project5.Pages.OpenAccountPage import OpenAccPage
from Selenium_Project5.Pages.RegisterPage import RegisterPage
from Selenium_Project5.Pages.TranferCompletePage import TransferCompletePage
from Selenium_Project5.Pages.TransferFund import TransferFund


def test_validation(driver):
    reg = RegisterPage(driver)
    reg.click_register()
    reg.verify_register_page()

    home = HomePage(driver)
    home.basic_details(
        "inder",
        "singh",
        "Gaur City",
        "Greater Noida",
        "Uttar Pradesh",
        "201009",
        "8383829292",
        "PIN483939",
        "inder_" + str(int(time.time())),  # unique username
        "New@123",
        "New@123"
    )
    home.register_btn()
    home.register_successfully()

    open_acc = OpenAccPage(driver)
    open_acc.click_open_account()
    open_acc.verify_open_account()

    open_acc_home =OpenAccHomePage(driver)
    open_acc_home.select_account_type("SAVINGS")
    open_acc_home.print_account_amount()
    open_acc_home.click_open_account_btn()

    acc_create = AccountCreated(driver)
    acc_create.verify_account_opened()
    acc_create.get_new_account_number()
    acc_create.click_transfer_fund()


    trans_fnd =TransferFund(driver)
    trans_fnd.trans_amount("500")
    trans_fnd.click_trans_btn()

    trans_complete_page = TransferCompletePage(driver)
    trans_complete_page.verify_transfer_heading()
    trans_complete_page.print_full_message()


