from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:


    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    
    checkbox= browser.find_element_by_id ('robotCheckbox').click()
    radiobatton= browser.find_element_by_id ('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobatton)
    radiobatton.click()
    x_element = browser.find_element_by_id('input_value')
    x_element = x_element.text
    print(x_element)
    y = calc(x_element) 
    
    print(y)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
   
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла