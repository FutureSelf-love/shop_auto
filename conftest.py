import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope="session")
def browser():
    path = r"E:\python softore test\jd_automation\chromedriver-win64\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(path))
    driver.maximize_window()
    yield driver
    driver.quit()
