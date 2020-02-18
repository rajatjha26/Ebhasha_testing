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
from comp_asTrans import trans_zar
from login import *

report=open("report.txt",'a')

def training(driver):
	report.write("\n")
	report.write("Testing Trainning Feature...")
	os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("select some text to highlight in training sample","Notification"))
	time.sleep(10)
	driver.find_element_by_id("markForTraining").click()
	time.sleep(6)
	report.write("OK")
	report.write("\n")
	return(driver)

def save(driver):
	time.sleep(2)
	report.write("\n")
	report.write("Testing Save Status feature...")
	driver.find_element_by_id("save").click()
	report.write("OK")
	report.write("\n")
	return(driver)

def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=training(driver1)
	time.sleep(2)
	driver1=save(driver1)
	time.sleep(2)
	driver1.close()	
