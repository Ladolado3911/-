import sys
import time
from Src.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
sys.path.append(sys.path[0] + "/....")


class Frame(object):
    def __init__(self, driver):
        self.driver = driver
        # elements
        self.plus_button = driver.find_element(By.XPATH, Locator.plus_button)
        self.option_button = driver.find_element(By.XPATH, Locator.option_button)
        self.cart_button = driver.find_element(By.XPATH, Locator.cart_button)
        driver.implicitly_wait(2)

    def test_image(self, image_src, element):
        new_image_src = str(element.get_attribute("src"))
        if new_image_src != image_src:
            print("Big picture changed")
        else:
            print("Big picture did not change")

        return new_image_src

    def test_images(self):
        image_src = ""
        for num in range(4):
            if num == 3:
                thumb = self.driver.find_element_by_id("thumb_1")
                self.test_image(image_src, thumb)
                thumb.click()
                time.sleep(1)
                break
            thumb = self.driver.find_element_by_id(f"thumb_{num + 2}")
            new_image_src = self.test_image(image_src, thumb)
            thumb.click()
            time.sleep(1)
            image_src = new_image_src
        self.driver.implicitly_wait(2)

    def add_to_cart(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.driver.implicitly_wait(2)
        self.plus_button.click()
        self.driver.implicitly_wait(2)
        self.option_button.click()
        self.driver.implicitly_wait(2)
        self.cart_button.click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()
        self.driver.implicitly_wait(5)

