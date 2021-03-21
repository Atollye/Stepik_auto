#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-


from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"



try: 
    driver = webdriver.Chrome()
    driver.get(link)

    input1=driver.find_element_by_xpath("//label[text()='First name*']/following-sibling::input")
    input1.send_keys("Anya")
    input2 = driver.find_element_by_xpath("//label[text()='Last name*']/following-sibling::input")
    input2.send_keys("Kuznetsova")
    input3 = driver.find_element_by_xpath("//label[text()='Email*']/following-sibling::input")
    input3.send_keys("alk@mail.ru")
    input4 = driver.find_element_by_xpath("//label[text()='Phone:']/following-sibling::input")
    input4.send_keys("79864586326")
    input5 = driver.find_element_by_xpath("//label[text()='Address:']/following-sibling::input")
    input4.send_keys("Moscow,Red Square, 1")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()



