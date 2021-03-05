from selenium import webdriver
import time
import math
def calc(x1,x2):
    return str(str(int(x1)+int(x2)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    x1 = browser.find_element_by_id ('num1')
    x1 = x1.text
    print (x1)
    x2 = browser.find_element_by_id ('num2')
    x2 = x2.text
    print (x2)
    
    x= calc(x1,x2)
    print (x)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value = '{x}'").click()


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла