# Scrapy Parser PEP

Парсер для сбора информации о PEP (Python Enhancement Proposals) с сайта [peps.python.org](https://peps.python.org/) с использованием фреймворка Scrapy.

## 📋 Описание

Парсер собирает данные о всех PEP:
- Номер PEP
- Название PEP
- Статус PEP

Результаты сохраняются в двух CSV-файлах:
1. **`pep_ДатаВремя.csv`** — список всех PEP с номерами, названиями и статусами
2. **`status_summary_ДатаВремя.csv`** — сводка по статусам с общим количеством

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <url-репозитория>
cd scrapy_parser_pep
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
# или
venv\Scripts\activate         # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск парсера

```bash
scrapy crawl pep
```

### 5. Результаты

После завершения работы в папке `results/` появятся два файла:

```
results/
├── pep_2026-06-20T12-00-00.csv
└── status_summary_2026-06-20T12-00-00.csv
```

## Тестирование

Запуск тестов:

```bash
pytest
```

## 📊 Пример выходных данных

### pep_*.csv

| number | name | status |
|--------|------|--------|
| 8 | Style Guide for Python Code | Active |
| 20 | The Zen of Python | Active |
| 391 | Dictionary-Based Configuration For Logging | Final |

### status_summary_*.csv

| Статус | Количество |
|--------|------------|
| Active | 30 |
| Final | 200 |
| Draft | 15 |
| Rejected | 50 |
| Total | 295 |

## 🔧 Технологии

- **Scrapy** — фреймворк для парсинга
- **SQLAlchemy** — не используется (данные сохраняются в CSV)
- **Python 3.12+**

## 📝 Автор

- Мария Кочнева
