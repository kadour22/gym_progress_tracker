FROM python:3.11-slim

RUN mkdir /apps
WORKDIR /apps

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt /apps/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /apps/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]