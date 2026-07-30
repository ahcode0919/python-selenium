from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """Base page object class"""

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))   
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)