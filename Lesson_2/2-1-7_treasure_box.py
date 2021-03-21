
# I am comment

import time, math
from selenium import webdriver


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    picture = browser.find_element_by_id("treasure")
    number = int(picture.get_attribute("valuex"))
    res = (lambda x: str(math.log(abs(12*math.sin(int(x))))))(number)
    text_field = browser.find_element_by_id("answer")
    text_field.send_keys(res)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio2 = browser.find_element_by_id("robotsRule")
    radio2.click()
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()