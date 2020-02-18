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

def Spell_check(driver):
	report.write("\n")
	report.write("Testing Spellchecker....")
	driver.find_element_by_xpath('//*[@id="lisc"]').click()
	for i in range(1,9):
		para='tgt'+str(i)+'sentence1'
		para_data= driver.find_element_by_id(para)
		para_data=para_data.text
		label= driver.find_element_by_id("scsrch")
		label.clear()
		word=para_data.strip()
		label.send_keys(word)
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='Spell Check']"))).click()
		time.sleep(2)

	driver.find_element_by_xpath('//*[@id="liclose"]').click()
	driver.find_element_by_xpath('//*[@id="tspellcheck"]').click()
	time.sleep(5)
	report.write("OK")
	report.write("\n")
	return(driver)

def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=Spell_check(driver1)
	time.sleep(2)
	driver1.close()
