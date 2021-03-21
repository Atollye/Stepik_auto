
# I am comment

import time, math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element_by_id("num1")
    number2 = browser.find_element_by_id("num2")
    result = str(int(number1.text)+int(number2.text))
    #browser.find_element_by_tag_name("select").click()
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    time.sleep(50)
    browser.quit()




