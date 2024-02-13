# Базовый образ с Python
FROM python:3.10.4-slim as builder

ENV POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PYTHONBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY poetry.lock pyproject.toml ./

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY . .

# Финальный образ
FROM python:3.10.4-slim
WORKDIR /app

RUN apt-get update && apt-get install -y libmariadb3 && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]