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

def GS(driver):
	report.write("\n")
	report.write("Testing Google Search....")
	os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Please,Select Keyword for Googling","Notification"))
	time.sleep(10)
	driver.find_element_by_id("gsearch").click()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(6)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	report.write("OK")
	report.write("\n")
	return(driver)

def GD(driver):
	report.write("\n")
	report.write("Testing Google Dictionary....")
	os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Please,Select Keyword for Google Dictionary","Notification"))
	time.sleep(10)
	driver.find_element_by_id("gdict").click()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(6)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	report.write("OK")
	report.write("\n")
	return(driver)

def Wiki(driver):
	report.write("\n")
	report.write("Testing Wikipedia Search...")
	os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Please,select Keyword for Wikipedia Search","Notification"))
	time.sleep(10)
	driver.find_element_by_id("wikipedia").click()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(6)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
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
	driver1=GS(driver1)
	time.sleep(2)
	driver1=GD(driver1)
	time.sleep(2)
	driver1=Wiki(driver1)
	time.sleep(2)
	driver1.close()


def gs():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=GS(driver1)
	time.sleep(2)
	driver1.close()
def gd():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=GD(driver1)
	time.sleep(2)
	driver1.close()
def wiki():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=Wiki(driver1)
	time.sleep(2)
	driver1.close()