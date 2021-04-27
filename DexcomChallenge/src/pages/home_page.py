import sys
sys.path.append(sys.path[0] + "/...")
from selenium.webdriver.common.by import By
from src.pages.locators import Locator


class HomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.link_elem = driver.find_element(By.LINK_TEXT,Locator.link_text)

    def getLinkElem(self):
        return self.link_elem

