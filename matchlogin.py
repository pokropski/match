from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv
from random import *

driver = webdriver.Chrome()
driver.get("http://www.match.com")
wait = WebDriverWait(driver, 10)

#login credentials
useremail = "pokropskitrainer@gmail.com"
userpassword = "thisismytestpass"



#click member link
assert "Match.com" in driver.title
link = driver.find_element_by_partial_link_text('Member')
link.click()

#insert email
email = driver.find_element_by_name('email')
email.clear()
email.send_keys(useremail)



#insert password
password = driver.find_element_by_name('password')
password.clear()
password.send_keys(userpassword)
password.send_keys(Keys.RETURN)


#stopped by captcha. unsure of how to proceed. attempted time.sleep() but even with 8 seconds of waiting still received captcha.
#could potentially point webdriver at local chrome profile, but not a scalable solution.


assert "https://www.match.com/home" in driver.current_url
