import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    request.cls.driver = driver
    yield driver
    driver.quit()