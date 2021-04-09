#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-
import time, math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINKS_LIST = [ "https://stepik.org/lesson/236895/step/1",
             "https://stepik.org/lesson/236896/step/1",
             "https://stepik.org/lesson/236897/step/1",
             "https://stepik.org/lesson/236898/step/1",
             "https://stepik.org/lesson/236899/step/1",
             "https://stepik.org/lesson/236903/step/1",
             "https://stepik.org/lesson/236904/step/1",
             "https://stepik.org/lesson/236905/step/1" ]

@pytest.fixture
def browser(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser

class TestFindMessages():

    def test_feedback_is_correct(self, browser):
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        answer = math.log(int(time.time()))
        textarea = WebDriverWait(browser, 7).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea")) )
        textarea.send_keys(str(answer))
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))   )
        button.click()
        hint = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located( (By.CSS_SELECTOR, ".smart-hints__feedback"))   )
        assert hint.text == "Correct!", f'Wrong text in hint "{hint.text}"'

# Автосворачивание строки на 79 символах в VS COde
