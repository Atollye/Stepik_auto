#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

"""
Задача:
https://stepik.org/lesson/138920/step/7?unit=196194
"""

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("Myau")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
   print(f'Произошла ошибка, вот её трэйсбэк: {error}')
   
finally:
    time.sleep(30)
    browser.quit()





