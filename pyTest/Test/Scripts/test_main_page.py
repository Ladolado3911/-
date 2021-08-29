import sys
import time
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.MainPage import MainPage
from Src.PageObject.Pages.Frame import Frame
from Src.PageObject.Pages.Frame2 import Frame2

sys.path.append(sys.path[0] + "/...")


class TestMainPage(WebDriverSetup):

    def test_Store_button(self):

        self.driver.get("http://automationpractice.com/index.php")
        self.driver.set_page_load_timeout(30)

        # Create an instance of the class so that you we can make use of the methods
        # in the class
        main = MainPage(self.driver)
        main.move_to_woman_button(self.action1)
        self.driver.implicitly_wait(5)
        main.click_tshirt_button()
        self.driver.implicitly_wait(10)

    def test_alert_frame(self):
        self.test_Store_button()
        main = MainPage(self.driver)
        main.go_to_frame(self.action2)
        frame = Frame(self.driver)
        frame.test_images()
        frame.add_to_cart()
        frame2 = Frame2(self.driver)
        frame2.return_from_frame()

    def test_casual_dress(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.set_page_load_timeout(30)
        self.driver.implicitly_wait(7)
        main = MainPage(self.driver)
        self.driver.implicitly_wait(7)
        main.move_to_woman_button(self.action3)
        main.click_casual_dresses_button()
        main.click_add_to_cart(self.action4)


if __name__ == '__main__':
    unittest.main()