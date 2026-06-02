import pytest
import os
from datetime import datetime
from selenium import webdriver
from pytest_html import extras


# ---------- DRIVER FIXTURE ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()


# ---------- DYNAMIC HTML REPORT ----------
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = os.path.join(reports_dir, f"report_{timestamp}.html")

    config.option.htmlpath = report_path
    config.option.self_contained_html = True


# ---------- SCREENSHOT ON FAILURE ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = os.path.join(
                screenshots_dir, f"{item.name}.png"
            )
            driver.save_screenshot(screenshot_path)

            report.extra = getattr(report, "extra", [])
            report.extra.append(extras.png(screenshot_path))