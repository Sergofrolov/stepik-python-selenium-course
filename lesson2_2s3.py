from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #расчёт суммы
    a_element = browser.find_element_by_id("num1")
    a = int(a_element.text)
    print (a)
    b_element = browser.find_element_by_id("num2")
    b = int(b_element.text)
    print(b)
    c = str(a+b)
    print (c)

    #Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(c)

    # нажимаем кнопку субмит
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
