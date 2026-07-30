from selenium import  webdriver


class UITest:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = None

    @classmethod
    def teardown_class(cls):
        cls.driver = None

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)

    def teardown_method(self, method):
        if self.driver:
            self.driver.quit()
