from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class MainPageLoginLogout(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    burger_menu_button = "bm-burger-button"
    logout_sidebar_link_id = "logout_sidebar_link"

    def login_main_page(self, user_nm, password):
        user_name = self.driver.find_element(By.NAME, "user-name")
        user_name.send_keys(user_nm)
        pass_word = self.driver.find_element(By.NAME, "password")
        pass_word.send_keys(password)
        self.driver.find_element(By.NAME, "login-button").click()

    def logout_main_page(self):
        self.driver.find_element(By.CLASS_NAME, self.burger_menu_button).click()
        self.driver.find_element(By.ID, self.logout_sidebar_link_id).click()
