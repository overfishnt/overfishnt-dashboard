FROM python:3.11.3-slim-buster

WORKDIR /app

COPY . .

RUN apt update

ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt

ENV HOST 0.0.0.0

EXPOSE 8080

CMD ["python3", "app.py"]
