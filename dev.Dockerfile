FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    netcat-openbsd \
    && apt-get clean

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN chmod +x /app/entrypoint.sh

EXPOSE 8050

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["gunicorn", "-c", "gunicorn_config.py", "django_settings.wsgi:application"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8050"]
