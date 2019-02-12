from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv

driver = webdriver.Chrome()
driver.get("http://www.match.com")
wait = WebDriverWait(driver, 10)

with open('matchcsv.csv') as file:
	csvdata=list(csv.reader(file))
	
		
#Modify this value to determine which row runs on the CSV
csvrow = 2

#Variables - do not modify
OS = csvrow - 1
usergengenseek = csvdata[OS][0]
zipcode = csvdata[OS][1]
useremail = csvdata[OS][2]
#password has a maximum of 16 characters
userpassword = csvdata[OS][3]
userbirthMonth = csvdata[OS][4]
userbirthDay = csvdata[OS][5]
userbirthyear = csvdata[OS][6]
userfirstname = csvdata[OS][7]
userlastname = csvdata[OS][8]

#click member link
assert "Match.com" in driver.title
link = driver.find_element_by_partial_link_text('Member')
link.click()

#click join link
assert "https://www.match.com/login/" in driver.current_url
link = driver.find_element_by_partial_link_text('Join for')
link.click()

#datingpreference
element = wait.until(EC.element_to_be_clickable((By.NAME, 'genderGenderSeek')))
usergenderseek = Select(driver.find_element_by_name('genderGenderSeek'))
usergenderseek.select_by_value(usergengenseek)

#insert zipcode
postalcode = driver.find_element_by_name('postalCode')
postalcode.clear()
postalcode.send_keys(zipcode)
button = driver.find_element_by_xpath('//button[contains(text(), "View Singles")]').click()

#insert email
element = wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
email = driver.find_element_by_name('email')
email.send_keys(useremail)
button = driver.find_element_by_xpath('//button[contains(text(), "Continue")]').click()


#insert password (DOES NOT HAVE AN ID)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
password = driver.find_element_by_name('password')
password.send_keys(userpassword)

#birthdaymonth
birthMonth = Select(driver.find_element_by_name('birthMonth'))
birthMonth.select_by_value(userbirthMonth)


#birthdayday (Selected by text as they are not listed as values)
birthday = Select(driver.find_element_by_name('birthDay'))
birthday.select_by_visible_text(userbirthDay)


#birthdayyear (Selected by text as they are not listed as values)
birthyear = Select(driver.find_element_by_name('birthYear'))
birthyear.select_by_visible_text(userbirthyear)
password.send_keys(Keys.RETURN)


#firstname (DOES NOT HAVE AN ID)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'firstname')))
firstname = driver.find_element_by_name('firstname')
firstname.send_keys(userfirstname)
firstname.send_keys(Keys.RETURN)


