from pages.page_base import PageBase
from pages.page_main import PageMain
from pages.page_settings import PageSettings
from pages.page_profile import PageProfile
from pages.page_signin import PageSignin


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.page_base = PageBase(self.driver)
        self.page_main = PageMain(self.driver)
        self.page_settings = PageSettings(self.driver)
        self.page_profile = PageProfile(self.driver)
        self.page_signin = PageSignin(self.driver)
