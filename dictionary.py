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
from comp_asTrans import trans_zar

report=open("report.txt",'a')

def dict1(driver):
	report.write("\n")
	driver.find_element_by_xpath('//*[@id="lidict"]').click()
	time.sleep(2)
	report.write("Testing Dictionary....")
	report.write("\n")
	dict_word=open("dict_test",'r')
	for word in dict_word:
		label= driver.find_element_by_id("dictsrch")
		label.clear()
		word=word.strip()
		label.send_keys(word)
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='Search']"))).click()
		time.sleep(1)
		dict_data= driver.find_element_by_id("dictview")
		word_mean=dict_data.text
		report.write(word)
		report.write("\n")		
		report.write(word_mean)
		report.write("\n")
	return(driver)

def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=dict1(driver1)
	time.sleep(3)
	driver1.close()