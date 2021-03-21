#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

"""
Задача:
1. Вам нужно открыть страницу http://suninjuly.github.io/simple_form_find_task.html 
2. Заполнить форму на этой странице с  помощью Selenium. 
3. Если всё сделано правильно, то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве ответа в этой задаче.
"""


import time
from selenium import webdriver


try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/find_xpath_form")
    input1=driver.find_element_by_tag_name("input")
    input1.send_keys("Anya")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Kuznetsova")
    input3 = driver.find_element_by_class_name("city")
    input3.send_keys("Moscow")
    input4 = driver.find_element_by_id("country")
    input4.send_keys("Russia")
    button = driver.find_element_by_xpath("//button[text()='Submit']")
    button.click()

except Exception as error:
   print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    time.sleep(10)
    driver.quit()




