from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.page_objects.base_page import BasePage
from tests.page_objects.mit_license_page import MitLicensePage


class HomePage(BasePage):
    COMMUNITY_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "community")
    GNU_GPL_V3_LINK_TEXT = (By.LINK_TEXT, "GNU GPLv3")
    HEADING = (By.TAG_NAME, "h1")
    MIT_LICENSE_LINK_TEXT = (By.LINK_TEXT, "MIT License")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_page_loaded(self):
        return "Choose an open source license" in self.find(self.HEADING).text

    def open_mit_license_page(self):
        self.find(self.MIT_LICENSE_LINK_TEXT).click()
        return MitLicensePage(self.driver)

    def open(self):
        self.get("https://choosealicense.com")
        return self
