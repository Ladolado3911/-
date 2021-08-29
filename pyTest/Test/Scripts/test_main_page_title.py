import sys
sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.MainPage import MainPage
import unittest
#from selenium import webdriver

class Store_Main_Page(WebDriverSetup):
    def test_Main_Page(self):
        driver = self.driver
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.set_page_load_timeout(30)

        web_page_title = "My Store"

        try:
            if driver.title == web_page_title:
                print("WebPage loaded successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        main_page = MainPage(driver)

if __name__ == '__main__':
    unittest.main()
