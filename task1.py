import requests
import pprint

# URL открытого API GitHub для поиска репозиториев
url = "https://api.github.com/search/repositories"

# Параметры запроса: ищем репозитории с кодом html
params = {
    'q': 'html'  # Поиск репозиториев с ключевым словом "html"
}

# Отправляем GET-запрос
response = requests.get(url, params=params)


# Печатаем статус-код ответа
print("Статус-код ответа:", response.status_code)

# Печатаем содержимое ответа в формате JSON
if response.ok:
    print(response.status_code)
    response_json = response.json()
    print("Содержимое ответа (JSON) через print(response.json()):")
    print(response_json)
    print("Содержимое ответа (JSON) через pprint.pprint(response_json):")
    pprint.pprint(response_json)
    print(f"Количество репозиториев с использованием js: {response_json['total_count']}")
    

else:
    print("Произошла ошибка при запросе данных.")

"""
### Объяснение кода:
1. Импортируем библиотеку `requests`.
2. Определяем URL для API GitHub для поиска репозиториев.
3. Указываем параметры запроса, в данном случае ищем репозитории, связанные с HTML.
4. Отправляем GET-запрос к API с параметрами.
5. Печатаем статус-код ответа, чтобы проверить, успешен ли был запрос.
6. Если статус-код 200 (успех), печатаем содержимое ответа в формате JSON. Если произошла ошибка, выводим соответствующее сообщение.

### Запуск кода:
Вы можете запустить этот код в вашей среде Python. Убедитесь, что у вас установлена библиотека `requests`. Если она не установлена, вы можете установить её с помощью команды:
```bash
pip install requests
```
"""