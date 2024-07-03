# Sprint_7

## Покрытие автотестами API сервиса "Яндекс Самокат"
https://qa-scooter.praktikum-services.ru/


1. Основа для написания автотестов — **pytest + requests + allure**
2. Перед началом работы необходимо установить зависимости:
```bash
pip install -r requirements.txt
```
3. Команда для запуска тестов с генерацией отчета:

```bash
pytest tests/ --alluredir=allure_results
```
4. Просмотр отчета:
```bash
allure serve allure_results 
```
В allure_results расположен последний сгенерированный отчет