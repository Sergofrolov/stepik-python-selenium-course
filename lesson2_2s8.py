from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #заполнить поля
    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys('Uaaa')
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys('Uaaa')
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys('Uaaa')

    #найти кнопку загрузки файла
    file = browser.find_element_by_id('file')

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, 'text.txt')
   
    #загружаем файл
    file.send_keys(file_path)
  
    # находим кнопку и нажимаем
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
