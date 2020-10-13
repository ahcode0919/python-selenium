from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class MitLicensePage(BasePage):
    HEADING_TAG = 'h1'
    LICENSE_ID = 'license-text'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_page_loaded(self):
        return 'MIT' in self.driver.find_element_by_tag_name(self.HEADING_TAG).text

    def license_text_displayed(self):
        return 'MIT License' in self.driver.find_element_by_id(self.LICENSE_ID).text

    def open(self):
        self.driver.get('https://choosealicense.com/licenses/mit/')
        return self
