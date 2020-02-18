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


def ConCordance(driver):
	report.write("\n")
	report.write("Testing Concordence....")
	driver.find_element_by_xpath('//*[@id="licc"]').click()
	time.sleep(2)
	report.write("\n")
	dict_word=open("concordence_src_test",'r')
	for word in dict_word:
		label= driver.find_element_by_id("ccsrch")
		label.clear()
		word=word.strip()
		label.send_keys(word)
		driver.find_element_by_xpath("//div[contains(@id,'cctab')]//button[contains(text(),'Search')]").click()
		data=driver.find_element_by_id("ccview")
		data=data.text
		report.write(word)
		report.write("\n")
		report.write(data)
		report.write("\n")
		time.sleep(2)
	driver.find_element_by_xpath('//*[@id="cc2"]').click()
	time.sleep(2)
	report.write("\n")
	dict_word=open("concordence_tgt_test",'r')
	for word in dict_word:
		label= driver.find_element_by_id("ccsrch")
		label.clear()
		word=word.strip()
		label.send_keys(word)
		driver.find_element_by_xpath("//div[contains(@id,'cctab')]//button[contains(text(),'Search')]").click()
		data=driver.find_element_by_id("ccview")
		data=data.text
		report.write(word)
		report.write("\n")
		report.write(data)
		report.write("\n")
		time.sleep(2)
	return(driver)


def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=ConCordance(driver1)
	time.sleep(2)
	driver1.close()