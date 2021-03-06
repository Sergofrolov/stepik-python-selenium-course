from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажать на кнопку
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    
    #перейти в новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #посчитать функцию
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    #код, который заполняет поле для ответа
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
  
    # находим кнопку и нажимаем
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
