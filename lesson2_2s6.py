from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Считать значение для переменной x и функцию от него
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #скроллим вниз страницу
    browser.execute_script("window.scrollBy(0, 150);")

    #код, который заполняет поле для ответа
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    #отметить чекбокс
    checkbox = browser.find_element_by_id ("robotCheckbox")
    checkbox.click()

    #отметить радио
    radio = browser.find_element_by_id ("robotsRule")
    radio.click()

    # находим кнопку и нажимаем
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
