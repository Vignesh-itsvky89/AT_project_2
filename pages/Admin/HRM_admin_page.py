from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AdminPage:
    admin = 'a[class="oxd-main-menu-item"]'
    user_management = "//span[text()='User Management ']"
    job = "//span[text()='Job ']"
    Organization = "//span[text()='Organization ']"
    Qualifications = "//span[text()='Qualifications ']"
    nationalities = "//a[text()='Nationalities']"
    Corporate_Banking = "//a[text()='Corporate Branding']"
    Configuration = "//span[text()='Configuration ']"

    def __init__(self, driver):
        self.driver = driver

    def select_Admin(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.admin))).click()

    def Admin_usermanagement(self):
        usermanagement = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.user_management))).text
        print(usermanagement)

    def Admin_job(self):
        job = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.job))).text
        print(job)

    def Admin_Organization(self):
        Organization = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Organization))).text
        print(Organization)

    def Admin_Qualifications(self):
        Qualifications = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Qualifications))).text
        print(Qualifications)

    def Admin_Nationalities(self):
        # Nationalities1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.nationalities))).text
        self.driver.find_element(By.XPATH,self.nationalities)
        # y= nationalities1.
        # print(Nationalities1)

    def Admin_Corporate_Banking(self):
        Corporate_Banking1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Corporate_Banking))).text
        print(Corporate_Banking1)

    def Admin_Configuration(self):
        Configuration = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Configuration))).text
        print(Configuration)







