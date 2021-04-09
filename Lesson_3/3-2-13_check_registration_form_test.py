#!/home/alayna/sel/ve/bin/python3
# -*- coding: utf-8 -*-
import time, unittest
from selenium import webdriver

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        driver = webdriver.Chrome()
        link = ("http://suninjuly.github.io/registration1.html")
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
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", f"Failed on page '{link}'")
        time.sleep(5)
        driver.quit()

    def test_registration2(self):
        driver = webdriver.Chrome()
        link = ("http://suninjuly.github.io/registration2.html")
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
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", f"Failed on page '{link}'")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    unittest.main()

