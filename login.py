from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
import os


def loginto_tool():
	report=open("report.txt",'w')
	options = webdriver.ChromeOptions()
	options.add_argument("--kiosk")
	driver = webdriver.Chrome(options=options)
	driver.get("http://ebhashasetu.com/ebhashalsp")
	assert "Login - Post edit Tool" in driver.title	
	user = "rajatjha46@gmail.com"
	pwd = ""	
	report.write("Login into eBhashaLSP....  ")
	elem = driver.find_element_by_id("username")
	elem.send_keys(user)
	elem = driver.find_element_by_id("password")
	elem.send_keys(pwd)
	elem.send_keys(Keys.RETURN)
	wait = WebDriverWait( driver, 5 )  
	try:
		page_loaded = wait.until(lambda driver: driver.title =='eBhashaLSP | Transeditor')
	except TimeoutException:
		self.fail( "Loading timeout expired" )
  
		self.assertEqual(driver.current_url,
		correct_page,
		msg = "Successful Login")
	report.write("Login Successful")
	report.write("\n")
	return(driver)

def fun():
	time.sleep(2)
	loginto_tool()
	time.sleep(5)
	driver.close()
