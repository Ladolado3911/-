import sys
import time
from Src.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
sys.path.append(sys.path[0] + "/....")


class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        # elements
        self.woman_button = driver.find_element(By.XPATH, Locator.woman_button)
        self.tshirt_button = driver.find_element(By.XPATH, Locator.tshirt_button)
        self.casual_dresses_button = driver.find_element(By.XPATH, Locator.casual_dresses_button)
        self.cart_button = driver.find_element(By.XPATH, Locator.cart_button)

        self.woman_image = driver.find_element(By.XPATH, Locator.woman_image)
        self.view_button = driver.find_element(By.XPATH, Locator.view_button)
        driver.implicitly_wait(2)

    def click_add_to_cart(self, action):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, Locator.woman_image2).click()
        time.sleep(2)
        self.driver.implicitly_wait(4)
        self.driver.switch_to.frame(0)
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, Locator.cart_button).click()
        self.driver.implicitly_wait(4)
        self.driver.switch_to.default_content()
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, Locator.continue_shopping_button).click()
        self.driver.implicitly_wait(4)
        action.move_to_element(self.driver.find_element(By.XPATH, Locator.cart)).perform()
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, Locator.checkout).click()
        self.driver.implicitly_wait(4)
        time.sleep(5)

    def move_to_woman_button(self, action):
        action.move_to_element(self.woman_button).perform()
        self.driver.implicitly_wait(4)

    def click_tshirt_button(self):
        self.tshirt_button.click()
        self.driver.implicitly_wait(4)

    def click_casual_dresses_button(self):
        self.casual_dresses_button.click()
        self.driver.implicitly_wait(4)

    def go_to_frame(self, action):
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.driver.implicitly_wait(2)
        action.move_to_element(self.woman_image).perform()
        self.driver.implicitly_wait(2)
        self.view_button.click()
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(0)
        self.driver.implicitly_wait(2)

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
