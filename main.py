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
from comp_asTrans import trans_zar,cat
from view_story import ViewStory
from login import *
from sidebar_fun import sidebar_function
from dictionary import dict1
from user_feed import Comment_fun,Rough_fun
from Concordance import ConCordance
from spell_checker import Spell_check
from task_info import task_stats,proj_guide,myqueries
from translitrate import word_transltr,char_transltr
from find_replace import find_replace
from External_dict import AMT,SMT,BMT,GMT,YMT,Shabd_kosh,Hin_wordnet
from Syndict import syndict
from TM import tm_fun
from search_ext import GS,GD,Wiki
from Save import training,save


driver1=loginto_tool()
time.sleep(2)

driver1=sidebar_function(driver1)
time.sleep(2)

driver1=ViewStory(driver1)
time.sleep(2)

driver1=trans_zar(driver1)

driver1=cat(driver1)
time.sleep(2)

driver1=dict1(driver1)
time.sleep(2)

driver1=Comment_fun(driver1)
time.sleep(2)

driver1=ConCordance(driver1)
time.sleep(2)

driver1=Spell_check(driver1)
time.sleep(2)

driver1=task_stats(driver1)
time.sleep(2)

driver1=Rough_fun(driver1)
time.sleep(2)

driver1=syndict(driver1)
time.sleep(2)

driver1=word_transltr(driver1)
time.sleep(2)

driver1=tm_fun(driver1)
time.sleep(2)

driver1=proj_guide(driver1)
time.sleep(2)

driver1.find_element_by_xpath('//*[@id="liclose"]').click()

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

driver1=GS(driver1)
time.sleep(2)

driver1=GD(driver1)
time.sleep(2)

driver1=Shabd_kosh(driver1)
time.sleep(2)

driver1=Hin_wordnet(driver1)
time.sleep(2)

driver1=Wiki(driver1)
time.sleep(2)

driver1=char_transltr(driver1)
time.sleep(2)
																
driver1=myqueries(driver1)
time.sleep(2)

driver1=training(driver1)
time.sleep(2)

driver1=save(driver1)
time.sleep(2)

driver1=find_replace(driver1)
time.sleep(2)

time.sleep(2)
driver1.close()