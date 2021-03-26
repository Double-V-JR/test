from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import math

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    btn1 = browser.find_element_by_css_selector('[onclick="checkPrice();"]')
    wait = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    btn1.click()
    x = int(browser.find_element_by_css_selector('#input_value').text)
    def log(x):
        return math.log(abs(12*math.sin(x)))
    y =  str(log(x))
    btn2 = browser.find_element_by_css_selector('#solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn2)
    input1 = browser.find_element_by_class_name('form-control')
    input1.send_keys(y)
    btn2.click()
finally:
    time.sleep(15)
    browser.quit()