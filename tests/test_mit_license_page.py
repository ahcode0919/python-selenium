from tests.page_objects.mit_license_page import MitLicensePage


class TestMitLicensePage:
    def test_license_text_displayed(self, driver):
        mit_license_page = MitLicensePage(driver).open()
        assert mit_license_page.license_text_displayed()
