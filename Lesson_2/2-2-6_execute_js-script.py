
import time
from math import log, sin
from selenium import webdriver
from selenium.webdriver.support.ui import Select


LINK = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(LINK)
    number = int(browser.find_element_by_id("input_value").text)
    res = (lambda x: log(abs(12*sin(x))))(number)
    textarea = browser.find_element_by_id("answer")
    textarea.send_keys(str(res))
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()





