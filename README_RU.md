# 🕵️ OSINT Automation Tools

Набор простых скриптов для автоматизации сбора информации из открытых источников (OSINT). Проект создаётся в учебных целях и предназначен для изучения основ OSINT с использованием Python.

---

## 📚 Оглавление

- [📖 Описание проекта](#-описание-проекта)
- [🛠️ Инструменты](#️-инструменты)
  - [🌐 Email Hunter](#-email-hunter)
  - [👤 Username Search](#-username-search)
  - [🌍 Domain Info](#-domain-info)
  - [📸 Image Analyzer](#-image-analyzer)
  - [🔑 Check Breach](#-check-breach)
  - [📞 Phone Lookup](#-phone-lookup)
- [🚀 Быстрый старт](#-быстрый-старт)
- [📂 Структура проекта](#-структура-проекта)
- [Отказ от ответственности](#️-отказ-от-ответственности)
  
---

## 📖 Описание проекта

Простой набор скриптов для автоматизации OSINT-задач. Всё максимально упрощено — никаких классов и сложных конструкций, только функции, которые можно запустить и сразу получить результат.

**Что умеет:**
- Собирать email-адреса с сайтов
- Проверять наличие username на соцсетях
- Получать WHOIS и DNS-информацию о домене
- Анализировать метаданные изображений
- Проверять пароли на утечки
- Определять страну по номеру телефона

---

## 🛠️ Инструменты

### 🌐 Email Hunter (`email_hunter.py`)

Собирает все email-адреса со страницы сайта.

```python
from email_hunter import get_emails

emails = get_emails("https://example.com")
print(emails)
# ['info@example.com', 'support@example.com']
```

### 👤 Username Search (`username_search.py`)

Проверяет наличие username на популярных платформах.

```python
from email_hunter import get_emails

emails = get_emails("https://example.com")
print(emails)
# ['info@example.com', 'support@example.com']
```

### 🌍 Domain Info (`domain_info.py`)

Получает WHOIS и DNS-информацию о домене.

```python
from domain_info import get_whois, get_dns

whois = get_whois("example.com")
dns = get_dns("example.com")
```
### 📸 Image Analyzer (`image_analyzer.py`)

Извлекает метаданные из изображений (EXIF, GPS-координаты).

```python
from image_analyzer import analyze_image

metadata = analyze_image("photo.jpg")
# {'Camera': 'Canon EOS', 'GPS': '48.8566, 2.3522', ...}
```

### 🔑 Check Breach (`check_breach.py`)

Проверяет, был ли пароль скомпрометирован (через Have I Been Pwned API).

```python
from check_breach import check_pwned

found, message = check_pwned("qwerty123")
print(message)  # 'Найден в 1234 утечках!' или 'Не найден в утечках'
```

### 📞 Phone Lookup (`phone_lookup.py`)

Определяет страну по номеру телефона.

```python
from phone_lookup import search_phone

info = search_phone("+7 123 456-78-90")
# {'country': 'Россия', 'clean': '71234567890', ...}
```

## 🚀 Быстрый старт

1. Клонирование
```bash
git clone https://github.com/st-b2/OSINT-Automation-Tools.git
cd OSINT-Automation-Tools
```
2. Установка зависимостей
```bash
pip install -r requirements.txt
```
3. Запуск
```bash
# Главное меню
python main.py

# Или отдельные скрипты
python email_hunter.py
python username_search.py
python domain_info.py
python image_analyzer.py
python check_breach.py
python phone_lookup.py
```
4. Пример работы
```bash
$ python main.py

==================================================
🕵️ OSINT Automation Tools
==================================================
1. Поиск email-адресов
2. Поиск по username
3. WHOIS домена
4. Проверка пароля на утечки
5. Выход
==================================================

Выберите действие: 1
Введите URL сайта: https://example.com

Найдено email: 3
  - info@example.com
  - admin@example.com
  - support@example.com
```
## 📂 Структура проекта

```text
📁 OSINT-Automation-Tools/
│
├── email_hunter.py      # Сбор email-адресов
├── username_search.py   # Поиск по username
├── domain_info.py       # Информация о домене
├── image_analyzer.py    # Анализ изображений
├── check_breach.py      # Проверка утечек
├── phone_lookup.py      # Поиск по номеру
├── main.py              # Главное меню
├── requirements.txt     # Зависимости
└── README.md
```

## ⚠️ Отказ от ответственности

Данный проект создан исключительно в образовательных целях. Используйте полученные знания и инструменты только для тестирования своих собственных систем или систем, на которые у вас есть письменное разрешение. Автор не несёт ответственности за использование предоставленной информации в незаконных целях.
