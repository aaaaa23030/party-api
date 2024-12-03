![Логотип проекта](images/logo.jpg)
# Party API
Бэкэнд для сайта по поиску и созданию вечеринок, основанный на REST API

## Описание
Этот проект представляет собой REST API для сайта с поиском и созданием вечеринок, разработанный с использованием Python и Django Rest Framework. Он позволяет создавать комнаты с вечеринками, заносить их в базу данных, получать все созданные комнаты с вечеринками, просматривать отдельные комнаты, а также удалять и изменять их. Реализована регистрация и авторизация по токенам.

## Технологии
- Python
- Django
- Django Rest Framework
- Djoser (пакет для аутентификации в Django)

## Установка
1. Склонируйте репозиторий
```commandline
git clone https://github.com/aaaaa23030/party-api.git
```
2. Создайте виртуальное окружение
```commandline
python -m venv venv
```

3. Активируйте виртуальное окружение
```
Если у вас Linux
source venv/Scripts/activate

Если у вас Windows
venv\Scripts\activate
```

4. Установите зависимости
```
pip install -r requirements.txt
```

5. Запустите сервер
```
python manage.py runserver
```

## Использование

### Эндпоинты

#### Роуты для комнат
- GET **/api/rooms/** - Получить список всех комнат с вечеринками
  
- POST **/api/rooms/** - Создать новую комнату с вечеринкой
  
- GET **/api/rooms/{id:int}/** - Получить данные об конкретной комнате с вечеринкой по её id

- PUT **/api/rooms/{id:int}/** - Обновить данные о комнате с вечеринкой по её id

- DELETE **/api/rooms/{id:int}/** - Удаление комнаты с вечеринкой по её id

#### Роуты для пользователей
- GET **/auth/users/** - Получить данные всех пользователей сайта
  
- POST **/auth/users/** - Регистрация нового пользователя

- GET **/auth/users/me/** -  Получить данные о пользователе по его авторизационному токену

- POST **/auth/token/login/** - Авторизация пользователя

- POST **/auth/token/logout/** - Выход из аккаунта

#### Аутентификация
Для всех роутов, кроме получения комнат, регистрации и авторизации требуется токен авторизации, его можно получить после авторизации на сайте. Передавайте токен в заголовках.

```json
"Authorization": "Token {Ваш токен}"
```

### Примеры запросов
____
- GET **/api/rooms/** - Получить список всех комнат с вечеринками

Тело ответа:
```json
[
    {
        "id": 6,
        "title": "Вечеринка с бассейном",
        "description": "ура вечеринка с басейном приходите к нам",
        "content": "📅 Дата: 20.01.2025  \n🕒 Время: 16:00  \n📍 Место: улица малышева\n\nЧто вас ждет на вечеринке? \n\nДжакузи",
        "photo": "{Путь до картинки}",
        "type": "актив",
        "alcohol": false,
        "age_restrictions": "<18",
        "gender": "мужчина",
        "members": 1,
        "user": 11
    },
]
```
_______
- POST **/api/rooms/** - Создать новую комнату с вечеринкой

Тело запроса:
```json
{
    "title" : "Название вечеринки",
    "description" : "Краткое описание вечеринки",
    "content" : "Полное описание вечеринки",
    "photo" : "Фотография вечеринки",
    "type" : "Тип вечеринки 'актив' или 'пасив'",
    "alcohol" : "True или False",
    "age_restrictions" : "Возрастные ограничения. >18 или <18>",
    "gender" : "пол. мужчина или женщина"
}
```

_______

- DELETE **/api/rooms/{id:int}/** - Удаление комнаты с вечеринкой по её id. Удалить комнату может только её владелец.

Тело запроса:
```json
{
    "id": "{id комнаты}",
    "Authorization": "Token {Ваш токен}"
}
```
________
- POST **/auth/users/** - Регистрация нового пользователя

Тело запроса:
```json
{
    "username": "{Имя пользователя}",
    "password": "{Пароль}"
}
```

- POST **/auth/token/login/** - Авторизация пользователя

Тело запроса:
```json
{
    "username": "{Имя пользователя}",
    "password": "{Пароль}"
}
```

Тело ответа:
```json
{
    "Authorization": "Token {Ваш токен}"
}
```



### Ошибки

| Код статуса | Описание                   |
|-------------|----------------------------|
| 200         | Успешный запрос            |
| 201         | Задача успешно создана     |
| 400         | Неверный запрос            |
| 404         | Задача не найдена          |
| 500         | Внутренняя ошибка сервера  |

## Авторы
**Максим Иванов Сергеевич**

