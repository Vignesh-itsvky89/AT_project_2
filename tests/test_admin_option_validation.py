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
from pages.Admin.HRM_admin_page import AdminPage

@pytest.fixture
def browser():
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

def test_PIM_02(browser):

    login_page = LoginPage(browser)
    login_page1 = AdminPage(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Click the "Sign in" button
    # HRM_login_page.click_sign_in_button()
    login_page.setUserName("Admin")
    login_page.setPassword("admin123")
    login_page.clickLogin()
    login_page1.select_Admin()
    # Click the "PIM" button to add Employee
    login_page1.Admin_usermanagement()
    try:
        print("User Management is displayed in admin page")
        if login_page1.Admin_usermanagement() == "User Management":
            print("User Management is displayed in admin page")
            assert True
    except:
        print("User Management is not displayed in admin page")
        assert False

    login_page1.Admin_job()
    try:
        print("Job is displayed in admin page")
        if login_page1.Admin_job() == "Job":
            assert True
    except:
        print("Job is not displayed in admin page")
        assert False

    login_page1.Admin_Organization()
    try:
        print("Organization is displayed in admin page")
        if login_page1.Admin_Organization() == "Organization":
            assert True
    except:
        print("Organization is not displayed in admin page")
        assert False

    login_page1.Admin_Qualifications()
    try:
        print("Qualifications is displayed in admin page")
        if login_page1.Admin_Qualifications() == "Qualifications":
            assert True
    except:
        print("Qualifications is not displayed in admin page")
        assert False

    login_page1.Admin_Nationalities()
    try:
        print("Nationalities is displayed in admin page")
        if login_page1.Admin_Nationalities() == "Nationalities":
            assert True
    except:
        print("Nationalities is not displayed in admin page")
        assert False

    login_page1.Admin_Corporate_Banking()

    if login_page1.Admin_Corporate_Banking() == "Corporate Banking":
        print("Corporate Banking is displayed in admin page")
        assert True
    else:
        print("Corporate Banking is not displayed in admin page")
        assert False

    login_page1.Admin_Configuration()
    try:
        print("Configuration is displayed in admin page")
        if login_page1.Admin_Configuration() == "Configuration":
            assert True
    except:
        print("Configuration is not displayed in admin page")
        assert False


