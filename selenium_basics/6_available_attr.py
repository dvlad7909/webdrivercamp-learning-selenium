from selenium import webdriver
from components.filter import LeftFilter

driver = webdriver.Chrome
left_filter = LeftFilter(driver)

# YOUR CODE HERE
print(dir(left_filter))
