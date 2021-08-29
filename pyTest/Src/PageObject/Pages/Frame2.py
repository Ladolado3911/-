import sys
import time
from Src.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
sys.path.append(sys.path[0] + "/....")


class Frame2(object):
    def __init__(self, driver):
        self.driver = driver
        # elements
        self.continue_button = driver.find_element(By.XPATH, Locator.continue_shopping_button)
        self.main_page_img = driver.find_element(By.XPATH, Locator.main_page_image)
        driver.implicitly_wait(2)

    def return_from_frame(self):
        self.driver.switch_to.default_content()
        self.driver.implicitly_wait(2)
        self.continue_button.click()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.implicitly_wait(2)
        self.main_page_img.click()
        self.driver.implicitly_wait(5)
