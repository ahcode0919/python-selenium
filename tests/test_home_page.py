from tests.page_objects.home_page import HomePage


class TestHomePage:
    def test_page_load(self, driver):
        home_page = HomePage(driver).open()
        assert home_page.is_page_loaded()

    def test_mit_page_link(self, driver):
        home_page = HomePage(driver).open()
        mit_license_page = home_page.open_mit_license_page()
        assert mit_license_page.is_page_loaded()
