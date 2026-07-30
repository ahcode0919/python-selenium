from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tests.page_objects.base_page import BasePage
from tests.page_objects.mit_license_page import MitLicensePage


class HomePage(BasePage):
    COMMUNITY_LINK_TEXT = (By.TEXT, 'community')
    GNU_GPL_V3_LINK_TEXT = 'GNU GPLv3'
    HEADING = 'h1'
    MIT_LICENSE_LINK_TEXT = 'MIT License'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_page_loaded(self):
        return "Choose an open source license" in self.driver.find_element_by_tag_name('h1').text

    def open_mit_license_page(self):
        self.driver.find_element_by_link_text(self.MIT_LICENSE_LINK_TEXT).click()
        return MitLicensePage(self.driver)

    def open(self):
        self.driver.get('https://choosealicense.com')
        return self

