import logging
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.utils import Util


class BaseDriver:
    log = Util.log_handling(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def find_and_scroll_to_given_element_id(self, element_id):
        scroll_element = self.driver.find_element(By.ID, element_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
        time.sleep(5)
        return scroll_element

    def wait_until_element_is_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_elements = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return list_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
