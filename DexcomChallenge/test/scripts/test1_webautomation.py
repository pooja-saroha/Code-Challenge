import sys

sys.path.append(sys.path[0] + "/...")

import unittest
from selenium import webdriver
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from time import sleep


class TestWebAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # chromedriver shd be in env PATH
        self.driver.get("https://clarity.dexcom.com/")
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()

    def test1_webautomation(self):

        page_title = "Dexcom CLARITY"

        try:
            if self.driver.title == page_title:
                print("WebPage Dexcom CLARITY loaded successfully")
                self.assertEqual(self.driver.title, page_title)
        except Exception as error:
            print(error + "WebPage Dexcom CLARITY Failed to load")

        # Create an instance of the page class
        home_page = HomePage(self.driver)

        # Click the "Dexcom CLARITY for Home Users" link to go to the next page
        home_page.getLinkElem().click()
        sleep(5)

        page_title = "Dexcom - Account Management"

        try:
            if self.driver.title == page_title:
                print("WebPage Dexcom - Account Management loaded successfully")
                self.assertEqual(self.driver.title, page_title)
        except Exception as error:
            print(error + "WebPage Dexcom - Account Management Failed to load")

        username = "codechallenge"
        password = "Password123"

        # Create an object of the Login Class
        login_page_obj = LoginPage(self.driver)
        sleep(5)

        # Fill in username/password and click login buttion
        login_page_obj.login_username_elem.send_keys(username)
        login_page_obj.login_password_elem.send_keys(password)
        login_page_obj.login_button_elem.click()
        sleep(3)

        # See if the login is successful
        # else report an Error
        page_title = "Dexcom CLARITY"

        try:
            if self.driver.title == page_title:
                print("User Logged in successfully")
                self.assertEqual(self.driver.title, page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

    def tearDown(self):
        if self.driver is not None:
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
