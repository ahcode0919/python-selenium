from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.page_objects.base_page import BasePage


class MitLicensePage(BasePage):
    HEADING_TAG = (By.TAG_NAME, "h1")
    LICENSE_ID = (By.ID, "license-text")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_page_loaded(self):
        return "MIT" in self.find(self.HEADING_TAG).text

    def license_text_displayed(self):
        return "MIT License" in self.find(self.LICENSE_ID).text

    def open(self):
        self.get("https://choosealicense.com/licenses/mit/")
        return self
