import softest
from selenium.webdriver.common.by import By
import logging
import time
import pytest

from pages.add_items_to_cart import ShoppingPage
from pages.portal_login_logout import MainPageLoginLogout
from utilities.utils import Util


@pytest.mark.usefixtures("setup")
class TestSelenium:
    log = Util.log_handling(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_main_page = MainPageLoginLogout(self.driver)
        self.logout_main_page = MainPageLoginLogout(self.driver)
        self.shoppingpage = ShoppingPage(self.driver)
        self.utility = Util()

    def test_login_as_visual_ser(self):
        # login_main_page = MainPageLoginLogout(self.driver)
        self.login_main_page.login_main_page("visual_user", "secret_sauce")
        time.sleep(5)

    def test_logout(self):
        # logout_main_page = MainPageLoginLogout(self.driver)
        self.logout_main_page.logout_main_page()
        time.sleep(5)

    def test_login_as_standard_ser(self):
        self.login_main_page.login_main_page("standard_user", "secret_sauce")
        time.sleep(5)

    @pytest.mark.usefixtures("start_test")
    def test_list_of_inventories_from_the_page(self):
        item_details = self.shoppingpage.list_items_available_in_shopping_page()
        logging.info(item_details)
        assert item_details

    def test_select_backpack_and_add_to_cart(self):
        self.shoppingpage.select_and_add_item_to_cart_using_item_id("add-to-cart-sauce-labs-backpack")

    def test_select_bikelight_and_add_to_cart(self):
        self.shoppingpage.select_and_add_item_to_cart_using_item_id("add-to-cart-sauce-labs-bike-light")

    def test_select_onesei_add_to_cart(self):
        self.shoppingpage.select_and_add_item_to_cart_using_item_id("add-to-cart-sauce-labs-onesie")

    def test_click_on_shopping_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "continue-shopping").click()

    def test_verify_shopping_cart(self):
        self.shoppingpage.wait_until_element_is_clickable(By.ID, "shopping_cart_container").click()
        time.sleep(5)
        self.shoppingpage.wait_until_element_is_clickable(By.ID, "continue-shopping").click()

    def test_verify_the_selected_items_added_to_cart(self):
        child_elements = self.shoppingpage.verify_number_of_items_in_cart()
        logging.info("Child elements")
        items = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Onesie"]
        for item in items:
            res = self.utility.verify_item_is_added_to_the_cart(item, child_elements)
            # self.soft_asert(self.assert_True, res)
            assert res, item+" is not added to the cart."
            # self.assert_all()
        self.log.info("TEST LOG MESSAGE")


# if __name__== "__main__":
#     main()