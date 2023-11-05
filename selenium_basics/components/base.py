from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    BASE_VAR = "Base Var"

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        __element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        __element.click()
