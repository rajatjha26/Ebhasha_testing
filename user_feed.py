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

def Comment_fun(driver):
	report.write("\n")
	report.write("Comment feature is tested....")
	report.write("\n")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='tfeedback']"))).click()
	time.sleep(2)
	driver.find_element_by_link_text("Insert Source").click()
	time.sleep(2)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='savefdb']"))).click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="lifb"]').click()
	time.sleep(2)
	return(driver)

def Rough_fun(driver):
	report.write("\n")
	report.write("Testing Rough feature ....")
	driver.find_element_by_xpath('//*[@id="lirp"]').click()
	time.sleep(1)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='Clear']"))).click()
	label=driver.find_element_by_id("roughpad")
	word="वशिष्ठ: मनाली से लगभग 3 किमी दूर, यह एक प्राचीन गांव है जो प्राकृतिक गर्म झरनों और ऋषि वशिष्ठ और भगवान राम को समर्पित प्राचीन पुराने मंदिरों के लिए लोकप्रिय है।"
	label.click()
	label.send_keys(word)
	driver.find_element_by_id('tgt1sentence1').click()
	time.sleep(1)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='Insert']"))).click()
	time.sleep(3)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='Clear']"))).click()
	time.sleep(3)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='Save']"))).click()
	time.sleep(3)
	report.write("OK")
	report.write("\n")
	return(driver)

def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=Comment_fun(driver1)
	time.sleep(3)
	driver1=Rough_fun(driver1)
	time.sleep(3)
	driver1.close()