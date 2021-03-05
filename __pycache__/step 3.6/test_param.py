from selenium import webdriver
import time
import math
import pytest



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.mark.parametrize('number1', ["895", "896","897","898","899","903","904","905"])
def test_guest(browser, number1):
    browser.implicitly_wait(10) 
    answer =str( math.log(int(time.time())))
    link = f"https://stepik.org/lesson/236{number1}/step/1"
    browser.get(link)
    
    input1= browser.find_element_by_tag_name("textarea")
    input1.send_keys(answer)
    button1 = browser.find_element_by_class_name("submit-submission").click()
    correct = browser.find_element_by_class_name("smart-hints__hint")
    assert correct.text == "Correct!",f"{correct.text}не равен Correct! "
    time.sleep(5)
    