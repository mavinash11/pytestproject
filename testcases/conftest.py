from selenium import webdriver
from selenium.webdriver.chrome.service import service as ChromeService
from selenium.webdriver.firefox.service import service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import logging


@pytest.fixture(scope="class")
def setup_old(request, browser):
    url = "https://www.saucedemo.com/"
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def setup(request):
    url = "https://www.saucedemo.com/"
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(autouse=False, scope="function")
def start_test():
    logging.info("Test Started")
