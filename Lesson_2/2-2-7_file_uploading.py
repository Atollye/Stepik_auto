#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

import os, time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    field1 = browser.find_element_by_name("firstname")
    field1.send_keys("Anna")
    field2 = browser.find_element_by_name("lastname")
    field2.send_keys("Kuznetsova")
    field3 = browser.find_element_by_name("email")
    field3.send_keys("nettie@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(current_dir)
    final_path = os.path.join(parent_dir, "data", "test_file.txt")
    file_field = browser.find_element_by_css_selector('[type="file"]')
    file_field.send_keys(final_path)    
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()



