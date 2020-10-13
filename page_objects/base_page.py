from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    """Base page object class"""

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
