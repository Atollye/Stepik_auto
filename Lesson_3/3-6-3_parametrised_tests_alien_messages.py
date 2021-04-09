#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-
import time, math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LINKS_LIST = [ "https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1" ]

#написать фикстуру, которая закрывает браузер, даже если тест упал

class TestFindMessages():

    def test_feedback_is_correct(self):
        link = "https://stepik.org/lesson/236895/step/1"
        browser = webdriver.Chrome()
        browser.get(link)
        answer = math.log(int(time.time()))
        time.sleep(5)
        textarea = browser.find_element(By.TAG_NAME, "textarea")
        textarea.send_keys(str(answer))
        time.sleep(10)
        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()
        time.sleep(5)
        hint = browser.find_element(By.CSS_SELECTOR, ".smart-hints__feedback")
        assert hint.text == "Correct!", f"Wrong text in hint {hint.text}"

# try:
#     button = browser.find_element_by_css_selector('[type="submit"]')
#     button.click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#     time.sleep(2)
#     number_field = browser.find_element_by_css_selector("#input_value")
#     number = number_field.text
#     res = calc(int(number))
#     field1 = browser.find_element_by_css_selector("#answer")
#     field1.send_keys(res)
#     button = browser.find_element_by_css_selector('[type="submit"]')
#     button.click()
# finally:
#     time.sleep(5)
#     browser.quit()


"""
???
Почему могут сущестовать тесты без Assert'a?
Вроде
    def test_feedback_is_correct(self):
        link = "https://stepik.org/lesson/236895/step/1"
        browser = webdriver.Chrome()
        browser.get(link)
        answer = math.log(int(time.time()))
        time.sleep(10)
        textarea = browser.find_element(By.TAG_NAME, "textarea")
        print(bool(textarea))
        browser.quit()
"""