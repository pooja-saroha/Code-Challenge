import sys
sys.path.append(sys.path[0] + "/...")
from selenium.webdriver.common.by import By
from src.pages.locators import Locator


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.login_username_elem = driver.find_element(By.XPATH,Locator.login_user_name)
        self.login_password_elem = driver.find_element(By.XPATH, Locator.login_password)
        self.login_button_elem = driver.find_element(By.XPATH, Locator.login_button)
