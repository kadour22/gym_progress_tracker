FROM python:3.11-slim

RUN mkdir /apps
WORKDIR /apps

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt /apps/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /apps/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]