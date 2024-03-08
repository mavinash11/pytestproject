from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
import time
import logging


class ShoppingPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    inventory_container_class_name = "//div[@class = 'inventory_container']/div"
    shopping_cart_container_id = "shopping_cart_container"
    cart_list_cls_name_in_shopping_cart = "cart_list"

    def verify_inventory_page_is_loaded(self):
        time.sleep(5)
        self.inventory_divs = self.driver.find_element(By.XPATH, self.inventory_container_class_name)
        return self.inventory_divs

    def select_and_add_item_to_cart_using_item_id_old(self, item_id="add-to-cart-sauce-labs-backpack"):
        pack_sizes_element = self.driver.find_element(By.ID, item_id)
        pack_sizes_element.send_keys(Keys.ENTER)

    def list_items_available_in_shopping_page(self):
        self.inventory_divs = self.driver.find_element(By.XPATH, self.inventory_container_class_name)
        # Get children of divs
        item_details={}
        children = self.inventory_divs.find_elements(By.XPATH, './child::*')
        for child in children:
            logging.info(child.id)
            logging.info(child.text)
            logging.info(child.get_attribute("innerHTML"))
            item_details[child.id] = child.text
        return item_details

    def select_and_add_item_to_cart_using_item_id(self, item_id="add-to-cart-sauce-labs-backpack"):
        element_id = self.find_and_scroll_to_given_element_id(item_id)
        element_id.send_keys(Keys.ENTER)

    def verify_number_of_items_in_cart(self):
        # self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.wait_until_element_is_clickable(By.ID, self.shopping_cart_container_id).click()
        cart_list = self.driver.find_element(By.CLASS_NAME, self.cart_list_cls_name_in_shopping_cart)
        child_elements = cart_list.find_elements(By.XPATH, "./child::*")
        return child_elements
