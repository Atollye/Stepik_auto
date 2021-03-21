#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

"""
Задание:

"""


import time, math
from selenium import webdriver

TEXT = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/find_link_text")
    link = driver.find_element_by_link_text(TEXT)
    link.click()
    input1=driver.find_element_by_tag_name("input")
    input1.send_keys("Anya")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Kuznetsova")
    input3 = driver.find_element_by_class_name("city")
    input3.send_keys("Moscow")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

except Exception as error:
   print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    time.sleep(10)
    driver.quit()