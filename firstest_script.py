import time
from selenium import webdriver # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By # импортируем класс By, который позволяет выбрать способ поиска элемента


try:
    driver = webdriver.Chrome() # инициализация драйвера браузера
    driver.get("https://suninjuly.github.io/text_input_task.html")
    time.sleep(5)

# СНАЧАЛА МЫ ВСЕГДА ИЩЕМ НУЖНЫЙ ЭЛЕМЕНТ, ВВЫБИРАЯ СПОСОБ ПОИСКА И НАЗВАНИЕ ЭЛЕМЕНТА
# ПОТОМ СОВЕРШАЕМ ДЕЙСТВИЯ С ПОМОЩЬЮ РАЗЛИЧНЫХ МЕТОДОВ: *элемент*.*действие* 

# find_element позволяет найти нужный элемент на сайте, указав путь к нему
# Метод принимает в качестве аргументов !способ поиска! и !значение!, по которому мы будем искать
# By.CSS_SELECTOR - способ; ".textarea" - значение
# Ищем поле для ввода текста
    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
# Напишем текст ответа в найденное поле
    textarea.send_keys("get()")
    time.sleep(5)

# Найдем кнопку, которая отправляет введенное решение
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
    submit_button.click()
    time.sleep(5)
finally:
# После выполнения всех действий мы должны не забыть закрыть окно браузера
    driver.quit()