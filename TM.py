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

def tm_fun(driver):
	report.write("\n")
	report.write("Testing Translation Memory Search ....")
	driver.find_element_by_xpath('//*[@id="litm"]').click()
	time.sleep(1)
	TM_word=open("TM",'r')
	for word in TM_word:
		label= driver.find_element_by_id("tmsrch")
		label.clear()
		word=word.strip()
		label.send_keys(word)
		driver.find_element_by_xpath("//div[contains(@id,'tmtab')]//button[contains(text(),'Search')]").click()
		time.sleep(1)
		TM_data2= driver.find_element_by_id("tmview2")
		word_mean=TM_data2.text
		report.write("\n")
		report.write(word_mean)
		report.write("\n")
		time.sleep(3)
	return(driver)

def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=tm_fun(driver1)
	time.sleep(2)
	driver1.close()