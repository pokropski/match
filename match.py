from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://www.match.com")

#click member link
assert "Match.com" in driver.title
link = driver.find_element_by_partial_link_text('Member')
link.click()

#click join link
assert "https://www.match.com/login/" in driver.current_url
link = driver.find_element_by_partial_link_text('Join for')
link.click()

#insert zipcode
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.NAME, 'postalCode')))
postalcode = driver.find_element_by_name("postalCode")
postalcode.clear()
postalcode.send_keys('75214')
