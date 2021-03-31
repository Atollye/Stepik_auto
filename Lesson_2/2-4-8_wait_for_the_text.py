#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

import os, time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    wait = WebDriverWait(browser, 12)
    condition = EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    wait.until(condition)
    button1 = browser.find_element_by_id("book")
    button1.click()
    number_field = browser.find_element_by_id("input_value")
    number = int(number_field.text)
    res = (lambda x: log(abs(12*sin(x))))(number)
    text_field = browser.find_element_by_id("answer")
    text_field.send_keys(str(res))
    button2 = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
finally:
    time.sleep(10)
    browser.quit()
