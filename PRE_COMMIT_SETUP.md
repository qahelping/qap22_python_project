# Инструкция по настройке Pre-commit

## Что такое Pre-commit?

Pre-commit — это инструмент для автоматической проверки и форматирования кода перед коммитом в Git. Он помогает поддерживать единый стиль кода и находить ошибки на раннем этапе.

## Установка Pre-commit

### 1. Установка зависимостей

Добавь `requirements.txt` в зависимости пакеты и установите их:
```bash
black== 25.9.0
flake8==7.3.0
isort==7.0.0
pre-commit==4.3.0

pip install -r requirements.txt
```

### 2. Установка Git hooks

После установки зависимостей установите Git hooks:

```bash
pre-commit install
```

Это создаст файлы в `.git/hooks/`, которые будут автоматически запускаться перед каждым коммитом.

### 3. Проверка установки

Проверьте, что hooks установлены корректно:

```bash
pre-commit --version
```

## Настройка Pre-commit в проекте

### Конфигурация

Конфигурация Pre-commit находится в файле `.pre-commit-config.yaml`. В проекте настроены следующие инструменты:

1. **Black** — форматирование кода Python
2. **isort** — сортировка импортов
3. **flake8** — проверка стиля кода и ошибок

### Параметры инструментов

#### Black

Настройки находятся в `pyproject.toml`:

```toml
[tool.black]
line-length = 90
target-version = ['py311']
```

#### isort

Настройки находятся в `pyproject.toml`:

```toml
[tool.isort]
profile = "black"
line_length = 88
```

#### flake8

Настройки находятся в `.flake8`:

```ini
[flake8]
max-line-length = 90
extend-ignore = E501, E203, W503, F811, E203, W503
```

## Использование Pre-commit

### Автоматический запуск

После установки hooks, Pre-commit будет автоматически запускаться при каждом коммите:

```bash
git add .
git commit -m "Your commit message"
```

Если проверки не пройдут, коммит будет отменен, и вам нужно будет исправить ошибки.

### Ручной запуск

Вы можете запустить проверки вручную для всех файлов:

```bash
pre-commit run --all-files
```

Или для конкретных файлов:

```bash
pre-commit run --files path/to/file.py
```

### Пропуск проверок (не рекомендуется)

Если необходимо пропустить проверки для конкретного коммита (не рекомендуется):

```bash
git commit --no-verify -m "Your commit message"
```

## Обновление Pre-commit hooks

Для обновления hooks до последних версий:

```bash
pre-commit autoupdate
```

Это обновит версии репозиториев в `.pre-commit-config.yaml` до последних доступных.
