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


def AMT(driver):
	report.write("\n")
	report.write("Testing Anusaaraka Translation....")
	driver.find_element_by_xpath('//*[@id="tdsrc4"]').click()
	time.sleep(3)
	driver.find_element_by_id("anutranslate").click()
	time.sleep(15)
	driver.switch_to.window(driver.window_handles[1])
	driver.find_element_by_id("kthlayer").click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@title="Select Sentence"]').click()
	time.sleep(1)
	driver.find_elements_by_xpath('//*[@class="text"]')[1].click()
	time.sleep(2)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	time.sleep(10)
	return(driver)

def SMT(driver):
	report.write("\n")
	report.write("Testing Sampark Machine Translation....")
	hin=driver.find_element_by_xpath('//*[@id="tgt4sentence1"]')
	hin.click()
	time.sleep(2)
	driver.find_element_by_id("samparktranslate").click()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(2)
	driver.find_element_by_xpath('//*[@title="Select pair"]').click()
	time.sleep(1)
	driver.find_elements_by_xpath('//*[@class="text"]')[1].click()
	time.sleep(1)
	driver.find_element_by_id("submit").click()
	time.sleep(12)
	select = Select(driver.find_element_by_id('savetype'))
	select.select_by_visible_text('.csv ')
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="download"]').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@title="Close"]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="edit"]').click()
	time.sleep(2)
	driver.switch_to.window(driver.window_handles[2])
	select = Select(driver.find_element_by_id('language'))
	time.sleep(1)
	select.select_by_visible_text('Hindi-WX')
	time.sleep(2)
	driver.close()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(2)
	driver.find_element_by_xpath('//*[@title="Hindi to Punjabi"]').click()
	time.sleep(1)
	driver.find_elements_by_xpath('//*[@class="text"]')[2].click()
	time.sleep(1)
	driver.find_element_by_id("submit").click()
	time.sleep(15)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	report.write("OK")
	report.write("\n")
	return(driver)

def GMT(driver):
	report.write("\n")
	report.write("Testing Google Translation....")
	driver.find_element_by_xpath('//*[@id="tdtgt11"]').click()
	time.sleep(1)
	driver.find_element_by_id("gtrans").click()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(6)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	report.write("OK")
	report.write("\n")
	return(driver)

def BMT(driver):
	report.write("\n")
	report.write("Testing Bing Machine Translation....")
	driver.find_element_by_xpath('//*[@id="tdtgt11"]').click()
	time.sleep(1)
	driver.find_element_by_id("bingtranslate").click()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(6)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	report.write("OK")
	report.write("\n")
	return(driver)

def YMT(driver):
	report.write("\n")
	report.write("Testing Yandex Machine Translation....")
	driver.find_element_by_xpath('//*[@id="tdtgt11"]').click()
	time.sleep(1)
	driver.find_element_by_id("yandextranslate").click()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(6)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	report.write("OK")
	report.write("\n")
	return(driver)

def Shabd_kosh(driver):
	report.write("\n")
	report.write("Testing Shabdkosh English2Hindi...")
	os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Please,Select Keyword for Shabdkosh English to Hindi","Notification"))
	time.sleep(10)
	driver.find_element_by_id("sdkosh").click()
	driver.switch_to.window(driver.window_handles[1])
	time.sleep(6)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	report.write("OK")
	report.write("\n")
	return(driver)

def Hin_wordnet(driver):
	report.write("\n")
	report.write("Testing Hindi Wordnet...")
	os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Please,Select Keyword for Hindi Wordnet","Notification"))
	time.sleep(10)
	driver.find_element_by_id("wordnet").click()
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
	driver1=AMT(driver1)
	time.sleep(2)
	driver1=SMT(driver1)
	time.sleep(2)
	driver1=GMT(driver1)
	time.sleep(2)
	driver1=BMT(driver1)
	time.sleep(2)
	driver1=YMT(driver1)
	time.sleep(2)		
	driver1=Shabd_kosh(driver1)
	time.sleep(2)
	driver1=Hin_wordnet(driver1)
	time.sleep(2)
	driver1.close()


def amt():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=AMT(driver1)
	time.sleep(2)
	driver1.close()
def smt():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1= SMT(driver1)
	time.sleep(2)
	driver1.close()
def gmt():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=GMT(driver1)
	time.sleep(2)
	driver1.close()
def bmt():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=BMT(driver1)
	time.sleep(2)
	driver1.close()
def ymt():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1= YMT(driver1)
	time.sleep(2)
	driver1.close()
def shabd():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=Shabd_kosh(driver1)
	time.sleep(2)
	driver1.close()
def hin_wordnet():
	driver1=loginto_tool()
	time.sleep(3)
	driver1=trans_zar(driver1)
	time.sleep(2)
	driver1.find_element_by_xpath('//*[@id="liclose"]').click()
	time.sleep(1)
	driver1=Hin_wordnet(driver1)
	time.sleep(2)
	driver1.close()	