from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_basics.components.base import Base
from selenium_basics.components.base import assert_text
from selenium_basics.components.filter import LeftFilter

driver = webdriver.Chrome()
main_page_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
driver.get(main_page_url)
search_param1 = "Rolex"
search_param2 = "Casio"
page = Base(driver)
panel = LeftFilter(driver)

# Initialising variables to store data

title_base = []
price_base = []
title_item = []
price_item = []

# ---------------TEST 1 Rolex title and price verification and text save----------------

# Check option 1

panel.select_option(search_param1)

# Get values of first two elements on the main page

for i in (0, 1):

    # Elements locators on base page

    title_path = "//ul[@class='srp-results srp-grid clearfix']/li[@data-viewport and @data-view][" + str(
                                       i + 1) + "]//span[@role='heading']"

    price_path = "//ul[@class='srp-results srp-grid clearfix']/li[@data-viewport and @data-view][" + str(
                                       i + 1) + "]//span[@class='s-item__price']"

    # Store base page text values

    title_base.append(page.get_text(title_path))
    price_base.append(page.get_text(price_path))

    # Select item

    page.click((By.XPATH, title_path))

    # Switch to item page

    driver.switch_to.window(driver.window_handles[i + 1])

    # Elements locators on item page

    title_path = "//h1[@class='x-item-title__mainTitle']/span"
    price_path = "//div[@class='x-price-primary']/span"

    # Store item page text values

    title_item.append(page.get_text(title_path))
    price_item.append(page.get_text(price_path))

    # Switch back to base page

    driver.switch_to.window(driver.window_handles[0])

# Assertions

for i in (0, 1):
    if not assert_text(search_param1.lower(), title_base[i].lower()):
        print(f"The option '{search_param1}' is NOT in title '{title_base[i]}'")
    if not assert_text(title_base[i], title_item[i]):
        print(f"The title on main page '{title_base[i]}' is NOT match the title on item page'{title_item[i]}'")
    if not assert_text(price_base[i], price_item[i]):
        print(f"The price on main page '{title_base[i]}' is NOT match the price on item page'{title_item[i]}'")

# Uncheck option 1

panel.select_option(search_param1)

# ----------- TEST 2 Casio title verification and text save-----------------

# Reset variable

title_base = []

# Check option 2

panel.select_option(search_param2)

# Get values of last two element on the main page

for i in (0, 1):

    # Elements locator on base page

    title_path = "//ul[@class='srp-results srp-grid clearfix']/li[@data-viewport and @data-view][last()-" + str(
        i) + "]//span[@role='heading']"

    # Save value

    title_base.append(page.get_text(title_path))

# Assertions

for i in (0, 1):
    if not assert_text(search_param2.lower(), title_base[i].lower()):
        print(f"The option '{search_param2}' is NOT in title '{title_base[i]}'")

# Close Chrome

driver.quit()
