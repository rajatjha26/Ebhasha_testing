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

def find_replace(driver):
	report.write("\n")
	report.write("Find and Replace testing....")
	driver.find_element_by_xpath('//*[@id="srchrep"]').click()
	time.sleep(1)
	driver.find_element_by_id("sarsrc").click()
	label= driver.find_element_by_id("search")
	label.clear()
	word="Manali"
	label.send_keys(word)
	label.click()
	for i in range(2):
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='↓']"))).click()
		time.sleep(1)
	for i in range(1):
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='↑']"))).click()
		time.sleep(1)
	driver.find_element_by_id("sartgt").click()
	label.clear()
	word="हिमाचल प्रदेश"
	label.send_keys(word)
	label.click()
	for i in range(2):
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='↓']"))).click()
		time.sleep(1)
	for i in range(1):
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='↑']"))).click()
		time.sleep(1)
	label= driver.find_element_by_id("replace_input")
	label.clear()
	word="हिमाद्रि"
	label.send_keys(word)
	for i in range(2):
		driver.find_element_by_id("replace").click()
		time.sleep(2)
	driver.find_element_by_id("replaceall").click()
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
	driver1=find_replace(driver1)
	time.sleep(2)
	driver1.close()	