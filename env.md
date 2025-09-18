1) Установка uv

brew install uv


2) Создать виртуалку в текущем репозитории

uv venv .venv
source .venv/bin/activate

3) Поставить зависимости

uv pip install -r requirements.txt

uv init           # создаст pyproject.toml
uv add fastapi    # пример; добавит зависимость и создаст uv.lock
uv add --dev ruff pytest

4) Настроить VS Code под это окружение

Создай .vscode/settings.json:

{
  "python.defaultInterpreterPath": ".venv/bin/python"
}

5) Как запускать

Без активации (удобно в задачах/скриптах):

uv run python main.py
uv run pytest
uv run uvx ruff check .

С активацией:

source .venv/bin/activate
python main.py
pytest