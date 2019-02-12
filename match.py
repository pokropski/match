from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.match.com")
assert "Match.com" in driver.title
link = driver.find_element_by_partial_link_text('Member')
link.click()
assert "https://www.match.com/login/" in driver.current_url
link = driver.find_element_by_partial_link_text('Join for')
link.click()
postalcode = find_element_by_id("postalcode")
postalcode.clear()
postalcode.send_keys("75214")
