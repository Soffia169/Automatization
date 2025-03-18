# Файлы:
***elements/baseElement.py*** содержит реализацию шаблона базового веб-элемента\
\
***pages/basePage.py*** содержит реализацию шаблона базовой веб-страницы\
***pages/mainSbisPage.py*** содержит реализацию шаблона главной веб-страницы сайта https://sbis.ru<br/>
\
***tests/test_Tensor.py*** содержит три Web UI теста\
\
***allure-results*** содержит результаты всех тестов\

# Запуск тестов:
**1. Установите все зависимости**
```python
pip install -r requirements
```
**2. Выполните команду в терминале для запуска тестов:**
```python
python -m pytest --alluredir allure-results
```
**3. Запустите генератор отчёта:**
```python
allure serve allure-results
```
