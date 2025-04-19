from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest 
import time

login_url = 'https://www.saucedemo.com/'
username = "standard_user"
password = 'secret_sauce'
expected_title = "Swag Labs"
expected_home_url = login_url
expected_dashboard_url = "https://www.saucedemo.com/inventory.html"

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_title(driver):
    driver.get(login_url)
    assert driver.title == expected_title, "Title does not match"

def test_homepage_url(driver):
    driver.get(login_url)
    assert driver.current_url == expected_home_url, "Homepage url does not match"

def test_login_and_dashboard_url(driver):
    driver.get(login_url)
    driver.find_element(By.ID, 'user-name').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(2)
    assert driver.current_url == expected_dashboard_url, "Dashboard URL mismatch"

    with open ("Webpage_task_11.txt", "w", encoding='utf-8') as file:
        file.write(driver.page_source)
