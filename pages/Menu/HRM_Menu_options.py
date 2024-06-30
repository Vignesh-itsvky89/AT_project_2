from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Menu_options:
    Admin = "// span[text() = 'Admin']"
    PIM = "//span[text()='PIM']"
    Leave = "//span[text()='Leave']"
    Time = "//span[text()='Time']"
    Recruitment = "//span[text()='Recruitment']"
    My_Info = "//span[text()='My Info']"
    Performance = "//span[text()='Performance']"
    Dashboard = "//span[text()='Dashboard']"
    Directory = "//span[text()='Directory']"
    Maintenance = "//span[text()='Maintenance']"
    Buzz = "//span[text()='Buzz']"


    def __init__(self, driver):
        self.driver = driver

    def Menu_Admin(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Admin)))

    def Menu_PIM(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.PIM)))

    def Menu_Leave(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Leave)))

    def Menu_Time(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Time)))

    def Menu_Recruitment(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Recruitment)))

    def Menu_My_Info(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.My_Info)))

    def Menu_Performance(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Performance)))

    def Menu_Dashboard(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Dashboard)))

    def Menu_Directory(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Directory)))

    def Menu_Maintenance(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Maintenance)))

    def Menu_Buzz(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Buzz)))



