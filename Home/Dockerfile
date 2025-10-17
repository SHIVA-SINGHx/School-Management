FROM python:3.10-slim

#environment variable

ENV PYTHONDONTWRITEBYCODE = 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# install dependency

COPY requirement.txt /app/
RUN pip install --upgrade pip && pip install -r requirement.txt
RUN pip install gunicorn

# static files

RUN python manage.py collectstatic --no-input --no-input