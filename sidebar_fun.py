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
report=open("report.txt",'a')

def sidebar_function(driver):
	report.write("opening sidebar.... ")
	driver.find_element_by_xpath('//*[@title="eBhasha Language Service Platform"]').click()
	report.write("OK")
	report.write("\n")
	time.sleep(2)


	report.write("Clicked on Statistic")
	report.write("\n")
	driver.find_element_by_xpath('//*[@title="View stats"]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@class="closebtn"]').click()
	time.sleep(1)
	select = Select(driver.find_element_by_id('prestat'))
	select.select_by_visible_text('Last 30 days')
	time.sleep(1)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default' and normalize-space()='GO']"))).click()
	time.sleep(1)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn' and normalize-space()='View']"))).click()
	time.sleep(4)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='close' and normalize-space()='×']"))).click()
	time.sleep(2)


	driver.find_element_by_xpath('//*[@title="eBhasha Language Service Platform"]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@title="View postedit log"]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@class="closebtn"]').click()
	time.sleep(4)


	driver.find_element_by_xpath('//*[@title="eBhasha Language Service Platform"]').click()
	driver.find_element_by_xpath('//*[@title="Click to View jobs"]').click()
	report.write("Clicked on view Jobs panel")
	report.write("\n")
	time.sleep(2)
	return(driver)


def fun():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=sidebar_function(driver1)
	time.sleep(3)
	driver1.close()