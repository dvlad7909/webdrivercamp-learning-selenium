from selenium_basics.components.base import Base
from selenium.webdriver.common.by import By


class LeftFilter(Base):
    LOCATOR = "//*"

    def __init__(self, driver):
        super().__init__(driver)

    def select_option(self, option, visible=False):
        locator_xpath = '//ul[@class="x-refine__left__nav"]/li//h3[text()="Brand"]/../..//span[text()="' + option + '"]/../../../span'
        Base.click(self, (By.XPATH, locator_xpath))
        # print(super().BASE_VAR)
        # print(self.LOCATOR)
        # print(option)
        # print(visible)