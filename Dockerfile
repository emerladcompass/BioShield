FROM python:3.9-alpine

WORKDIR /app

# تثبيت المتطلبات النظامية
RUN apk add --no-cache gcc musl-dev linux-headers

# نسخ المتطلبات أولاً (لتحسين caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ الكود
COPY src/ ./src/
COPY config.json .
COPY README.md .

# نقطة الدخول
ENTRYPOINT ["python", "-m", "src.main"]
