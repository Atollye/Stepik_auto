#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

import os, time
from math import log, sin
from selenium import webdriver
from Stepik_auto.utils.utils import calc

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name('button').click()
    browser.switch_to.window(browser.window_handles[1])
    number_field = browser.find_element_by_id("input_value")
    number = int(number_field.text)
    res = (lambda x: log(abs(12*sin(x))))(number)
    field1 = browser.find_element_by_css_selector("#answer")
    field1.send_keys(str(res))
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()

