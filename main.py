from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://sbis.ru")  # Переход на веб-страницу

element = driver.find_element(By.XPATH, "//*[@id='wasaby-content']")  # Получение ссылки Контакты
print(element)
element.click()