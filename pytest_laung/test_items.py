import time
import math
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_checking_the_bucket(browser):
    browser.get(link)
    time.sleep(5)
    assert  browser.find_element_by_css_selector("button.btn:nth-child(3)")
    