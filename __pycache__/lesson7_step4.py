from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1 = browser.find_element_by_id ("book")
    button1.click()
    
    x= browser.find_element_by_id ("input_value")
    x= x.text
    y= calc(x)
    input1= browser.find_element_by_tag_name("textarea").click()
    input1.send_keys(y)    
    button = browser.find_element_by_id("solve")
   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()