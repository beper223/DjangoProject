# ---------- Этап сборки ----------
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Системные зависимости для сборки
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt


# ---------- Этап рантайма ----------
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Только runtime зависимости
RUN apt-get update && apt-get install -y \
    libpq5 \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Создаём пользователя
RUN addgroup --system django && adduser --system --ingroup django django

# Копируем зависимости
COPY --from=builder /install /usr/local

# Копируем проект
COPY . .

# Копируем entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Сбор статики (ВАЖНО — до USER)
#RUN python manage.py collectstatic --noinput

RUN chown -R django:django /app

USER django

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

#CMD ["gunicorn", "core.wsgi:application",
#     "--bind", "0.0.0.0:8000",
#     "--workers", "3",
#     "--threads", "2",
#     "--timeout", "120",
#     "--access-logfile", "-",
#     "--error-logfile", "-"]

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
