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
from login import loginto_tool

report=open("report.txt",'a')



def ViewStory(driver):
	driver.find_element_by_xpath('//*[@class="closebtn"]').click()
	driver.find_element_by_xpath('//*[@title="view"]').click()
	report.write("view clicked")
	report.write("\n")
	time.sleep(2)


	report.write("\n")
	driver.find_element_by_xpath('//*[@id="viewstory"]').click()
	report.write("story_opened")
	report.write("\n")
	time.sleep(2)


	driver.find_element_by_xpath('//*[@class="close"]').click()
	report.write("story-closed")
	report.write("\n")
	time.sleep(2)
	return(driver)

def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=ViewStory(driver1)
	time.sleep(3)
	driver1.close()