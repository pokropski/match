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

with open('matchcsv.csv') as file:
	csvdata=list(csv.DictReader(file))

#Modify this value to determine which row runs on the CSV
csvrow = 2

#Variables - do not modify
emailx = randint(8000000, 90000000)  #needed for email
OS = csvrow - 1
usergengenseek = csvdata[OS]["usergengenseek"]
zipcode = csvdata[OS]["zipcode"]
useremail = csvdata[OS]["useremail"]
#password has a maximum of 16 characters
userpassword = csvdata[OS]["userpassword"]
userbirthMonth = csvdata[OS]["userbirthmonth"]
userbirthDay = csvdata[OS]["userbirthday"]
userbirthyear = csvdata[OS]["userbirthyear"]
userfirstname = csvdata[OS]["userfirstname"]
userlastname = csvdata[OS]["userlastname"]

#click member link
assert "Match.com" in driver.title
link = driver.find_element_by_partial_link_text('Member')
link.click()

#click join link
assert "https://www.match.com/login/" in driver.current_url
#this page takes a long time to load. not sure of cause.
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
email.send_keys(useremail + '+' + str(emailx) + '@gmail.com')
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
#Can't send return from this section. Have to do it from the password field. should clean up in the future to avoid confusion
password.send_keys(Keys.RETURN)


#firstname (DOES NOT HAVE AN ID)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'firstname')))
firstname = driver.find_element_by_name('firstname')
firstname.send_keys(userfirstname)
firstname.send_keys(Keys.RETURN)

#let's get started
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_3C16hUu')))
button = driver.find_element_by_class_name("_3C16hUu").click()

#Could not figure out how to select from these same class items. My knowledge of automation runs dry here
#as I am unsure of how to continue without IDs or names for selectors. Chose the 'skip' option

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_38avMfQ')))
button = driver.find_element_by_class_name("_38avMfQ").click()

#I had an issue where I could not select the class within the larger class without running into a conflict.
#This also skips this question
time.sleep(.5)
button = driver.find_element_by_class_name("_38avMfQ").click()
