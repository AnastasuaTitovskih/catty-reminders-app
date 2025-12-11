FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем ВСЕ нужные файлы
COPY app/main_lab4.py app/
COPY templates/ templates/
COPY config.json .

EXPOSE 8181

CMD ["uvicorn", "app.main_lab4:app", "--host", "0.0.0.0", "--port", "8181"]
