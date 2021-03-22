from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #дождаться цены в 100$
    price = WebDriverWait(browser, 15).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "$100")
      )

    #Нажать на кнопку book
    button = browser.find_element_by_css_selector("#book")
    button.click()
    
    #посчитать функцию
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #код, который заполняет поле для ответа
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
  
    # находим кнопку submit и нажимаем
    button = browser.find_element_by_css_selector("#solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
