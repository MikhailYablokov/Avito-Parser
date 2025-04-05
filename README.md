# Тестовое задание: Парсинг Avito и веб-интерфейс для загрузки XML

Этот проект представляет собой решение тестового задания для Python-разработчика, включающего парсинг данных с Avito и интеграцию с веб-интерфейсом для загрузки XML-файлов.

## Описание проекта

Проект состоит из двух основных частей:
1. **Парсер Avito** (`avito_parser.py`) — скрипт для сбора данных о недвижимости в ЮФО с сайта Avito.
2. **Веб-приложение** (`main.py`) — FastAPI-приложение с веб-интерфейсом для загрузки XML-файлов и проверки уникальности объявлений.

### Задача 1: Парсинг данных с Avito
- **Цель**: Сбор объявлений о продаже квартир в регионах ЮФО.
- **Поля**: Заголовок, цена, адрес, площадь (м²), ссылка, дата публикации.
- **Выходной формат**: XML-файлы с именем `avito_{region}_{годмесяцдень_часыминуты}.xml`.
- **Особенности**:
  - Используется библиотека `seleniumbase` для парсинга динамического контента.
  - Обработка ошибок (таймауты, ограничение доступа).
  - Сохранение данных по 2000 объявления в файл.

### Задача 2: Интеграция XML с веб-интерфейсом
- **Цель**: Загрузка XML-файлов через веб-интерфейс с проверкой дубликатов.
- **Технологии**: FastAPI, Jinja2, HTML.
- **Проверка уникальности**: Объявления считаются дубликатами, если совпадают URL или комбинация заголовка и адреса.
- **Интерфейс**: Простая HTML-форма с отображением статуса загрузки.

## Как запустить проект
### Требования
- Python 3.8+
- Установленные зависимости: `pip install -r requirements.txt`
  - fastapi
  - uvicorn
  - jinja2
  - seleniumbase
  - loguru

### Запуск парсера
Выполните команду:
   ```bash
   python avito_parser.py
```
Запуск веб-приложения
---

Выполните в консоли:
```bash
uvicorn main:app --reload
```
- Откройте в браузере: http://127.0.0.1:8000.

Структура проекта
---
```
project_root/
├── static/              # Статические файлы (CSS, JS)
├── templates/           # HTML-шаблоны
│   └── upload_form.html # Форма загрузки
|   └── upload.html
├── main.py              # FastAPI-приложение
├── avito_parser.py      # Парсер Avito
├── ads.json             # Хранилище загруженных объявлений
└── README.md            # Документация
```
