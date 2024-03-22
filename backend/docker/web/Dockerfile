FROM python:3.11 AS base

WORKDIR /app
ADD . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./docker/web/backend.sh /backend.sh
RUN sed -i 's/\r$//g' /backend.sh && chmod +x /backend.sh

ENTRYPOINT ["/backend.sh"]