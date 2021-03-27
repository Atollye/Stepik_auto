#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

import os, time
from selenium import webdriver
from Stepik_auto.utils.utils import calc

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)
    number_field = browser.find_element_by_css_selector("#input_value")
    number = number_field.text
    res = calc(int(number))
    field1 = browser.find_element_by_css_selector("#answer")
    field1.send_keys(res)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()



#C:\Users\User\PycharmProjects\main\venv
