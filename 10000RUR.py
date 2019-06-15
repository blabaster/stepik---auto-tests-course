from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Забронировать"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR'))
browser.find_element_by_id('book').click()
s = browser.find_element_by_id('input_value').text
browser.find_element_by_id('answer').send_keys(str(log(abs(12. * sin(int(s))))))
browser.find_element_by_id('solve').click()