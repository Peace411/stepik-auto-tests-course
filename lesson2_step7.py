from selenium import webdriver
import time
import os 
try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    input1 = browser.find_element_by_name ('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name ('lastname')
    input2.send_keys("Ivan")
    input3 = browser.find_element_by_name ('email')
    input3.send_keys("Ivan")
    file1 = browser.find_element_by_id ('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file1.send_keys(__file__)
    button = browser.find_element_by_class_name ('btn-primary').click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
