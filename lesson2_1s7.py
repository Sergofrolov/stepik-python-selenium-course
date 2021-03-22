from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #расчёт функции
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    print (x)
    y = calc(x)

    #код, который заполняет  поля
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    #отметить чекбокс
    checkbox = browser.find_element_by_id ("robotCheckbox")
    checkbox.click()

    #отметить радио
    radio = browser.find_element_by_id ("robotsRule")
    radio.click()

    # нажимаем кнопку субмит
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
