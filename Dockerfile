FROM python:3.12.7-alpine 

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libpq \
    postgresql-dev \
    build-base \
    linux-headers \
    python3-dev \
    libffi-dev \
    py3-setuptools

RUN pip install --upgrade pip setuptools wheel

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]