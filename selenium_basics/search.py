from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.ebay.com")
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.ID, 'gf-AdChoice')))
print(driver.current_url)
elem = driver.find_element(By.XPATH, "//input[@aria-label='Search for anything']")
elem.send_keys("women watch")
driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()
assert "women watch" == driver.find_element(By.XPATH, "//h1[@class='srp-controls__count-heading']/span[2]").text
driver.close()