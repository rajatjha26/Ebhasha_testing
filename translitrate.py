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

def word_transltr(driver):
	report.write("\n")
	report.write("Testing TransLitrate ....")
	driver.find_element_by_xpath('//*[@id="litransliterate"]').click()
	time.sleep(1)
	dict_word=open("dict_test",'r')
	for word in dict_word:
		label= driver.find_element_by_id("translsrch")
		label.clear()
		word=word.strip()
		label.send_keys(word)
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='Submit']"))).click()
		time.sleep(1)
		dict_data= driver.find_element_by_id("transtab")
		word_mean=dict_data.text
		report.write(word)
		report.write("\n")
		report.write(word_mean)
		report.write("\n")
	return(driver)


def char_transltr(driver):
	report.write("\n")
	report.write("Testing Character Transliteration...")
	os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Please,select Text for Charcater Transliteration","Notification"))
	time.sleep(10)
	driver.find_element_by_id("charactertranslation").click()
	time.sleep(6)
	report.write("OK")
	report.write("\n")
	return(driver)

def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=word_transltr(driver1)
	time.sleep(2)	
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=char_transltr(driver1)
	time.sleep(2)
	driver1.close()