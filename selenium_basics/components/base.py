from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome


def assert_text(text_value_1, text_value_2):
    try:
        assert text_value_1 in text_value_2
        return True
    except AssertionError:
        return False


class Base:
    BASE_VAR = "Base Var"

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, path):
        text_v = self.driver.find_element(By.XPATH, path)
        return text_v.text
