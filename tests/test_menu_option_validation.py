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
from pages.Menu.HRM_Menu_options import Menu_options

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

def pytest_configure(config):
    config.option.htmlpath = '/path/to/report.html'

def test_PIM_03(browser):

    login_page = LoginPage(browser)
    login_page1 = Menu_options(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Click the "Sign in" button
    # HRM_login_page.click_sign_in_button()
    login_page.setUserName("Admin")
    login_page.setPassword("admin123")
    login_page.clickLogin()

    login_page1.Menu_Admin()
    try:
        print("Admin is displayed in Menu options")
        if login_page1.Menu_Admin() == "Admin":
            assert True
    except:
        print("Admin is not displayed in Menu options")
        assert False
    login_page1.Menu_PIM()
    try:
        print("PIM is displayed in Menu options")
        if login_page1.Menu_PIM() == "PIM":
            assert True
    except:
        print("PIM is not displayed in Menu options")
        assert False

    login_page1.Menu_Leave()
    try:
        print("Leave is displayed in Menu options")
        if login_page1.Menu_Leave() == "Leave":
            assert True
    except:
        print("Leave is not displayed in Menu options")
        assert False

    login_page1.Menu_Time()
    try:
        print("Time is displayed in Menu options")
        if login_page1.Menu_Time() == "Time":
            assert True
    except:
        print("Time is not displayed in Menu options")
        assert False

    login_page1.Menu_Recruitment()
    try:
        print("Recruitment is displayed in Menu options")
        if login_page1.Menu_Recruitment() == "Recruitment":
            assert True
    except:
        print("Recruitment is not displayed in Menu options")
        assert False

    login_page1.Menu_My_Info()
    try:
        print("My Info is displayed in Menu options")
        if login_page1.Menu_My_Info() == "My Info":
            assert True
    except:
        print("My Info is not displayed in Menu options")
        assert False

    login_page1.Menu_Performance()
    try:
        print("Performance is displayed in Menu options")
        if login_page1.Menu_Performance() == "Performance":
            assert True
    except:
        print("Performance is not displayed in Menu options")
        assert False

    login_page1.Menu_Dashboard()
    try:
        print("Dashboard is displayed in Menu options")
        if login_page1.Menu_Dashboard() == "Dashboard":
            assert True
    except:
        print("Dashboard is not displayed in Menu options")
        assert False

    login_page1.Menu_Directory()
    try:
        print("Directory is displayed in Menu options")
        if login_page1.Menu_Directory() == "Directory":
            assert True
    except:
        print("Directory is not displayed in Menu options")
        assert False

    login_page1.Menu_Maintenance()
    try:
        print("Maintenance is displayed in Menu options")
        if login_page1.Menu_Maintenance() == "Maintenance":
            assert True
    except:
        print("Maintenance is not displayed in Menu options")
        assert False

    login_page1.Menu_Buzz()
    try:
        print("Buzz is displayed in Menu options")
        if login_page1.Menu_Buzz() == "Buzz":
            assert True
    except:
        print("Buzz is not displayed in Menu options")
        assert False

