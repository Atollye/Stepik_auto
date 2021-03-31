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
    # Тег, присутствующий на странице
    # <input class="form-check-input" type="radio" name="ruler" id="peopleRule" value="people" checked="">
    radio1 = driver.find_element_by_id("peopleRule")
    # Атрибут у тега есть и у атрибута есть значение: возвращает его значение,
    # в данном случае people
    radio1_value = radio1.get_attribute("value")
    print(radio1_value)
    # Атрибут у тега есть, но без значения: возвращает true
    radio1_checked = radio1.get_attribute("checked")
    print(radio1_checked)
    # Атрибута у тега нет: возвращает None
    radio1_enabled = radio1.get_attribute("enabled")
    print(radio1_enabled)

finally:
    time.sleep(5)
    driver.quit()

 

