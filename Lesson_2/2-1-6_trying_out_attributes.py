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
    radio1 = driver.find_element_by_id("peopleRule")
    # radio1_checked = radio1.get_attribute("checked")
    # print(radio1_checked)
    # radio1_enabled = radio1.get_attribute("enabled")
    # print(radio1_enabled)
    radio1_value = radio1.get_attribute("value")
    print(radio1_value)

finally:
    time.sleep(5)
    driver.quit()

 

