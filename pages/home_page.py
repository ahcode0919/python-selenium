from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from pages.mit_license_page import MitLicensePage


class HomePage(BasePage):
    COMMUNITY_LINK_TEXT = 'community'
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

