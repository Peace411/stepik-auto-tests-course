from selenium import webdriver
import time 
import unittest
class Testauth(unittest.TestCase):
    def test_registration1(self):
         link = "http://suninjuly.github.io/registration1.html"
         browser = webdriver.Chrome()
         browser.get(link)
         input1 = browser.find_element_by_css_selector('.first_block > .first_class > .first')
         input1.send_keys("Ivan")
         input2 = browser.find_element_by_css_selector('.first_block > .second_class > .second')
         input2.send_keys("Ivanov")
         input3 = browser.find_element_by_class_name('third')
         input3.send_keys("@ynadex.ru")
         button = browser.find_element_by_css_selector("button.btn")
         button.click()
         time.sleep(1)
         welcome_text_elt = browser.find_element_by_tag_name("h1")
         welcome_text = welcome_text_elt.text
         self.assertEqual("Congratulations! You have successfully registered!",welcome_text,f"Текст{welcome_text} отличается от ожидаемого ")
        
    def test_registration2(self):
         link = "http://suninjuly.github.io/registration2.html"
         browser = webdriver.Chrome()
         browser.get(link)
         input1 = browser.find_element_by_css_selector('.first_block > .first_class > .first')
         input1.send_keys("Ivan")
         input2 = browser.find_element_by_css_selector('.first_block > .second_class > .second')
         input2.send_keys("Ivanov")
         input3 = browser.find_element_by_class_name('third')
         input3.send_keys("@ynadex.ru")
         button = browser.find_element_by_css_selector("button.btn")
         button.click()
         time.sleep(1)
         welcome_text_elt = browser.find_element_by_tag_name("h1")
         welcome_text = welcome_text_elt.text
         self.assertEqual("Congratulations! You have successfully registered!",welcome_text,f"Текст{welcome_text} отличается от ожидаемого ")     
if __name__ == "__main__": unittest.main()