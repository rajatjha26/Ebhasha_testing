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

def syndict(driver):
	report.write("\n")
	report.write("Testing SynDict feature ....")
	driver.find_element_by_xpath('//*[@id="lisyndict"]').click()
	time.sleep(1)
	syn_word=open("syn_dict",'r')
	for word in syn_word:
		label= driver.find_element_by_id("syndictsrch")
		label.clear()
		word=word.strip()
		label.send_keys(word)
		time.sleep(2)
		driver.find_element_by_xpath("//div[contains(@id,'syndicttab')]//button[contains(text(),'Search')]").click()
		time.sleep(2)
	report.write("OK")
	report.write("\n")
	return(driver)


def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=syndict(driver1)
	time.sleep(2)
	driver1.close()