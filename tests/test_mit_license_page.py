from page_objects.base_page import BasePage
from page_objects.mit_license_page import MitLicensePage
from setup.setup import UITest


class TestMitLicensePage(UITest):
    def test_license_text_displayed(self):
        mit_license_page = MitLicensePage(self.driver).open()
        assert mit_license_page.license_text_displayed()