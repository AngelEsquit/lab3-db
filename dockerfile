FROM python:3.13-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY data.sql /data.sql

ENV PYTHONPATH=/code

RUN apt-get update && apt-get install -y postgresql-client

CMD ["python", "-m", "app.database"]