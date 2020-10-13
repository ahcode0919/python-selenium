from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class UITest:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = None

    @classmethod
    def teardown_class(cls):
        cls.driver = None

    def setup_method(self, method):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(15)

    def teardown_method(self, method):
        self.driver.quit()
