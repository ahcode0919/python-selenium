from page_objects.home_page import HomePage
from setup.setup import UITest


class TestHomePage(UITest):
    def test_page_load(self):
        home_page = HomePage(self.driver).open()
        assert home_page.is_page_loaded()

    def test_mit_page_link(self):
        home_page = HomePage(self.driver).open()
        mit_license_page = home_page.open_mit_license_page()
        assert mit_license_page.is_page_loaded()
