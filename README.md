# LLM Service
**Production-ready LLM API service with RAG, FastAPI, and modern AI stack.**

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com)
[![uv](https://img.shields.io/badge/uv-0.4+-purple.svg)](https://github.com/astral-sh/uv)

## Описание

**LLM Service** — это высокопроизводительный REST API для работы с большими языковыми моделями.

**Возможности:**
- ✅ Поддержка OpenAI, Anthropic, Ollama
- ✅ RAG (Retrieval-Augmented Generation)
- ✅ Векторный поиск через Qdrant
- ✅ Асинхронная обработка запросов
- ✅ Кеширование и управление контекстом
- ✅ Метрики качества (RAGAS)
- ✅ Контейнеризация (Docker)

## Технологический стек

| Компонент | Технология |
| :--- | :--- |
| **Язык** | Python 3.12 |
| **Фреймворк** | FastAPI |
| **Менеджер зависимостей** | uv |
| **База данных** | PostgreSQL + pgvector |
| **Векторная БД** | Qdrant |
| **LLM** | OpenAI / Ollama / Anthropic |
| **Оркестрация** | Docker / Docker Compose |


## Быстрый старт

### Требования

- Python 3.12+
- Docker (опционально)
- [uv](https://github.com/astral-sh/uv)

### Установка

```bash
# Клонирование репозитория
git clone https://github.com/your-username/llm-service.git
cd llm-service

# Установка зависимостей
uv sync

# Копирование переменных окружения
cp .env.example .env
```
                  
### Запуск

```bash
# Локальный запуск
uv run main.py

# Запуск через Docker
docker-compose up
```
                  
### Проверка

```bash
curl http://localhost:8000/health
```

## Примеры использования

### Генерация текста
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explain what is RAG in simple terms.",
    "model": "gpt-4o",
    "max_tokens": 200
  }'

                  
Ответ:

{
  "status": "success",
  "response": "RAG (Retrieval-Augmented Generation) is a technique...",
  "model": "gpt-4o",
  "tokens_used": 198
}
```
                  
### RAG-запрос
```bash
curl -X POST http://localhost:8000/rag \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the key features?",
    "collection": "docs",
    "top_k": 3
  }'
```

## Структура проекта
```bash                  
llm-service/
├── .github/ # GitHub Actions workflows
├── src/
│ ├── init.py
│ ├── main.py # FastAPI приложение
│ ├── api/ # Роуты
│ │ ├── init.py
│ │ ├── endpoints/
│ │ │ ├── generation.py
│ │ │ └── rag.py
│ │ └── models.py # Pydantic модели
│ ├── core/ # Бизнес-логика
│ │ ├── llm.py # LLM клиенты
│ │ └── rag.py # RAG логика
│ ├── db/ # Базы данных
│ │ ├── postgres.py
│ │ └── qdrant.py
│ └── config.py # Настройки
├── tests/ # Тесты
│ ├── init.py
│ └── test_generation.py
├── docker/
│ ├── Dockerfile
│ └── docker-compose.yml
├── .env.example # Шаблон переменных окружения
├── .gitignore
├── .python-version
├── pyproject.toml # Зависимости
├── uv.lock # Lock файл
└── README.md
```

## ‍Разработка

### Установка dev-зависимостей
```bash
uv sync --with dev
```
                  
### Запуск тестов
```bush
uv run pytest -v --cov=app
```
                  
### Форматирование кода
```bush
uv run black .
uv run ruff check --fix .
```
                  
### Проверка типов
```bash
uv run mypy .
```

## Лицензия

```markdown
MIT License. См. [LICENSE](LICENSE) для деталей.
```