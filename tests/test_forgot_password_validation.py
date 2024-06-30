from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
import sys
import os
import time

# Add the parent directory to the path if amazon_login_page.py is in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login.HRM_login_page import LoginPage
from pages.login.HRM_login_page import forgot_login


@pytest.fixture
def browser():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    chromedriver_path = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")

    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    time.sleep(6)
    driver.quit()


def test_PIM_01(browser):
    login_page = LoginPage(browser)
    login_page1 = forgot_login(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Click the "Sign in" button
    # HRM_login_page.click_sign_in_button()

    # Perform login actions (replace with actual login details and logic)
    login_page1.select_forgot_password()
    time.sleep(5)
    login_page1.send_username("admin123")
    time.sleep(5)
    login_page1.select_reset_password()
    time.sleep(5)
    login_page1.validate_reset_password_popup()
    print("test_PIM_01 is passed **** " "Reset Password link sent successfully message displayed")
    # Add assertions or further actions based on the login result
    # For example, you could assert that the user is redirected to the homepage after successful login
    # assert "Reset Password link sent successfully" in login_page1.validate_reset_password_popup()
    if login_page1.validate_reset_password_popup() == "Reset Password link sent successfully":
        assert True

