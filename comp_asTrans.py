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
from login import *

report=open("report.txt",'a')
# loginto_tool()

def trans_zar(driver):
	report.write("\n")
	report.write("Transzar opened")
	driver.find_element_by_xpath('//*[@title="edit"]').click()
	report.write("\n")
	time.sleep(2)
	return(driver)
def cat(driver):
	report.write("\n")
	report.write("Testing Computer Assisted Translation....")
	driver.find_element_by_xpath('//*[@id="tdsrc6"]').click()
	report.write("\n")
	time.sleep(2)	
	hin_data=driver.find_element_by_xpath('//*[@id="mttext1"]')
	hin_data=hin_data.text
	data=driver.find_element_by_xpath('//*[@id="src6sentence1"]').text
	report.write(str(data))
	report.write("\n")
	report.write(str(hin_data))
	report.write("\n")
	return(driver)

def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=cat(driver1)
	time.sleep(2)
	driver1.close()