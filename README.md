# Проєкт **«Технічний магазин»**  
Практикум від **Light IT Global**

![Made with Python](https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

> Демонстраційний бекенд для інтернет-магазину з використанням **Django**, **Unfold** та **Django REST Framework**.

## 📄 Технічне завдання

Проєкт реалізовано відповідно до прикладного [технічного завдання](https://github.com/serhiichyrva123/practicum/blob/main/terms-of-reference.md).

## 📑 Зміст

- [Опис проєкту](#опис-проєкту)
- [Функціональні можливості](#функціональні-можливості)
- [Запуск проєкту](#запуск-проєкту)
- [Ліцензія](#ліцензія)

## 📌 Опис проєкту

Реалізація бекенд-частини демо-версії сайту «Технічний магазин» з:

- Адмін-панеллю на основі **Django + Unfold**
- API на основі **Django REST Framework** з JWT-автентифікацією
- Інтерактивною документацією **SwaggerUI**

## 📦 Функціональні можливості

- Повний функціонал згідно з [технічним завданням](https://github.com/serhiichyrva123/practicum/blob/main/terms-of-reference.md)
- Стилізована адмін-панель **Django** для управління магазином
- API з JWT-авторизацією та документацією на **SwaggerUI**
- Команди для завантаження тестових даних та користувачів

## ⚙️ Запуск проєкту

1. Клонуйте репозиторій: <br>```git clone https://github.com/serhiichyrva123/practicum.git```
2. Встановіть залежності: <br>```pip install -r requirements``` або ```poetry install```
3. Виконайте міграції: <br>```python manage.py migrate```
4. Створіть користувача-адміна: <br>```python manage.py createsuperuser```
5. Завантажте фікстури та тестових користувачів: <br>```python manage.py load_fixtures```
<br>```python manage.py register_test_users -p <PASSWORD>```
6. Запустіть сервер: <br>```python manage.py runserver```

### Доступи:
* Адмін-панель: https://127.0.0.1:8000/admin
* Swagger документація API: https://127.0.0.1:8000/api/docs

## 📄 Ліцензія

Проєкт поширюється на умовах **MIT License**.

```text
MIT License

Copyright (c) 2025 Serhii Chyrva

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[<img src="https://user-images.githubusercontent.com/89206401/168461242-884f25ce-eb67-406a-9d98-cf8d0f28cb43.png" width=100>](https://github.com/serhiichyrva123/practicum/blob/main/LICENSE)
