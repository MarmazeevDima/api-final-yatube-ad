FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app

WORKDIR /app/yatube_api

COPY README.md /app/yatube_api/README.md

CMD sh -c "pytest /app/tests -v && python manage.py runserver 0.0.0.0:8000"