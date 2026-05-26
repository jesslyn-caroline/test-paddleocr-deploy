FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libgomp1 \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--workers=1", "--threads=2", "--worker-class=gthread", "--timeout=120", "--bind=0.0.0.0:8080", "app:app"]