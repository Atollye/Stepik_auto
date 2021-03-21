#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-

"""
Задание: написать скрипт, который откроет следующий шаг в данном уроке на Stepik и отправит правильное решение в задаче.
"""

import time

from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)


driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)


textarea = driver.find_element_by_css_selector(".textarea")
textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element_by_css_selector(".submit-submission")
submit_button.click()
time.sleep(5)

driver.quit()
