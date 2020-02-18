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

def task_stats(driver):
	report.write("\n")
	report.write("Task Stats.....")
	driver.find_element_by_xpath('//*[@id="lits"]').click()
	time.sleep(2)
	report.write("OK")
	report.write("\n")
	return(driver)

def proj_guide(driver):
	report.write("\n")
	report.write("Project Guidelines.....")
	driver.find_element_by_xpath('//*[@id="lipg"]').click()
	time.sleep(2)
	report.write("OK")
	report.write("\n")
	return(driver)

def myqueries(driver):
	report.write("\n")
	report.write("Testing MyQueries.....")
	os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Ask Queries by selecting text","Notification"))
	time.sleep(5)
	driver.find_element_by_id("querysaver").click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="submitQuery"]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="limyqueries"]').click()
	time.sleep(2)
	driver.find_element_by_id("view2").click()
	time.sleep(2)
	driver.find_element_by_xpath("//div[contains(@id,'answerstab')]//button[contains(text(),'Close')]").click()
	report.write("OK")
	report.write("\n")
	return(driver)


def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1=task_stats(driver1)
	time.sleep(2)
	driver1=proj_guide(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	driver1=myqueries(driver1)
	time.sleep(2)
	driver1.close()