#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

import math, time

from selenium import webdriver

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    driver = webdriver.Chrome()
    driver.get(link)
    number_field = driver.find_element_by_id("input_value")
    number = int(number_field.text)
    result = calc(number)
    answer_field = driver.find_element_by_id("answer")
    answer_field.send_keys(result)
    checkbox = driver.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = driver.find_element_by_id("robotsRule")
    radiobutton.click()
    submit_button = driver.find_element_by_css_selector(".btn-default")
    submit_button.click()

finally:
    time.sleep(5)
    driver.quit()

 

