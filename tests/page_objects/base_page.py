from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base page object class"""

    def __init__(self, driver: WebDriver, wait_time: int = 10):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, wait_time)

    def find(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def get(self, url: str):
        self.driver.get(url)
        return self

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
